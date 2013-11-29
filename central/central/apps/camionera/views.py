from django.shortcuts import render_to_response
from central.apps.camionera.models import *
from django.template import *
from central.apps.camionera.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def ciudadesView(request):
	ciudades  = ciudad.objects.all()
	return render_to_response('camionera/ciudad.html',{'ciudades':ciudades},context_instance=RequestContext(request))

def viajesView(request):
	viajes = viaje.objects.filter(status=True)
	paradas = ruta_parada.objects.all()

	ctx = {'viajes':viajes,'paradas':paradas}
	return render_to_response('camionera/viajesTrue.html',ctx, context_instance=RequestContext(request))

def choferesView(request):
	chof = chofer.objects.all()
	ctx = {'chof':chof}
	return render_to_response('camionera/choferes.html',ctx, context_instance=RequestContext(request))

def camionesView(request):
	cam =camion.objects.all()
	ctx = {'cam':cam}
	return render_to_response('camionera/camiones.html',ctx, context_instance=RequestContext(request))

def consultaDatosViaje(request, id):
	via = viaje.objects.get(id=id)
	paradas = ruta_parada.objects.all()

	capacidad = via.camion.capacidad
	contador = via.contados
	disponibles = capacidad - contador

	ctx = {'via':via, 'paradas':paradas, 'disponibles': disponibles}
	return render_to_response('camionera/consultaViaje.html',ctx, context_instance=RequestContext(request))

def historialViajes(request):
	viaj = viaje.objects.all()
	paradas = ruta_parada.objects.all()
	ctx = {'v':viaj,'paradas':paradas}
	return render_to_response('camionera/historialViajes.html',ctx,context_instance=RequestContext(request))

def reservacionesView(request):
	reserv = reservacion.objects.filter(status=False)
	ctx = {'reserv':reserv}
	return render_to_response('camionera/reservaciones.html',ctx,context_instance=RequestContext(request))


def formReservacion(request, id):
	via = viaje.objects.get(id=id)
	inc = str(via.contados)
	clave = (via.ruta.origen.nombre[0:3].lower()+via.ruta.destino.nombre[0:3].lower()+via.chofer1.nombre[0:3].lower()+via.chofer1.apellidoP[0:3].lower()+inc)
	if request.method == 'POST':
		formulario = reservacionForm(request.POST)
		if formulario.is_valid():
			formulario.save(commit=False)
			#obtener ultima reservacion registrada			
			ultimo = reservacion.objects.all().count()
			#obtener el id del viaje de la ultima reservacion
				
			viajez = reservacion.objects.filter(id=ultimo).values('viaje')
			v = viajez[0] ['viaje']
						
			#contador			
			conta = viaje.objects.filter(id=id).values('contados')
			cont = conta [0] ['contados']
			
			cami = viaje.objects.filter(id=id).values('camion')
			cam = cami [0] ['camion']
			
			capa = camion.objects.filter(id=cam).values('capacidad')
			cap = capa [0] ['capacidad']
			
			if cont >= cap:
				return HttpResponseRedirect('/URLERROR_AUTOBUSLLENO')
			else:
				reserv = reservacion()
				nom = formulario.cleaned_data['nombre']
				aps = formulario.cleaned_data['apellidos']
				reserv.nombre = nom
				reserv.apellidos = aps
				reserv.viaje = via
				reserv.status = False
				reserv.fechaAbordar = via.fechaSalida
				reservactual = reservacion.objects.all().count()+1
				reservactual = str(reservactual)
				#clave = (nom[0:2].lower()+aps[0:2].lower()+via.ruta.origen.nombre[0:3].lower()+reservactual+via.ruta.destino.nombre[0:3].lower()+id)
				reserv.clave = clave
				reserv.save()
				viaje.objects.filter(id=id).update(contados = cont + 1)
				return HttpResponseRedirect('/reservaciones')
	else:
		formulario = reservacionForm()
	return render_to_response('camionera/Freservacion.html',{'formulario':formulario,'viaje':via, 'clave': clave}, context_instance = RequestContext(request))

	
def formParada(request):
	if request.method == 'POST':
		formulario = paradaForm(request.POST)
		if formulario.is_valid():
			formulario.save(commit=False)

			#obtener ultima parada registrada
			
			ultimo = viaje_parada.objects.all().count()
			
			#obtener el viaje al que pertenece
			
			viajp = viaje_parada.objects.filter(id = ultimo).values('viaje')
			vp = viajp [0] ['viaje']
			
			#obtener el id de la parada
			
			rutaPar = viaje_parada.objects.filter(id = ultimo).values('rutaParada')
			rupar = rutaPar [0] ['rutaParada']
			
			#obtener la ciudad de la parada, a partir del id de la parada
			
			ciudadpar = ruta_parada.objects.filter(id = rupar).values('parada')
			cpar = viajp [0] ['parada']
			
			#obtener las reservaciones del viaje con destino en la ciudad de la parada y que hayan abordado
			
			personas = reservaciones.objects.filter(viaje = vp).filter(destino = cpar).filter(status=True).count()
			
			#contador actual del camion
			
			conta = viaje.objects.filter(id=vp).values('contados')
			cont = cont [0] ['contados']
			
			#resta del contador menos las personas que acaban de bajar

			cont = cont - personas
			
			#commits 
			#NO TERMINADO
			
			return HttpResponseRedirect('/cuentas')
	else:
		formulario = paradaForm()
	return render_to_response('camionera/Fparada.html',{'formulario':formulario}, context_instance = RequestContext(request))

	
def formAbordar(request, id):
	res = reservacion.objects.get(id=id)
	if request.method == 'POST':
		formulario = abordarForm(request.POST)
		if formulario.is_valid():
			abor = abordar()
			abor.reservacion = res
			abor.status = True
			abor.save()
			reser = reservacion()
			res.status = True
			res.save()
			return HttpResponseRedirect('/reservaciones')
	else:
		formulario = abordarForm()
	return render_to_response('camionera/Fabordar.html',{'res':res}, context_instance = RequestContext(request))


def formChofer(request):
	if request.method == 'POST':
		formulario = choferForm(request.POST, request.FILES)
		if formulario.is_valid():
			nombre = formulario.cleaned_data['nombre']
			apellidoP = formulario.cleaned_data['apellidoP']
			apellidoM = formulario.cleaned_data['apellidoM']
			imagen = formulario.cleaned_data['imagen']
			p = chofer()
			p.nombre =nombre
			p.apellidoP = apellidoP
			p.apellidoM = apellidoM
			p.status = True
			if imagen:
				p.imagen = imagen
			p.save()
			return HttpResponseRedirect('/choferes')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('camionera/FChoferes.html',ctx,context_instance=RequestContext(request))
	else:
		formulario = choferForm()
	ctx = {'formulario':formulario}
	return render_to_response('camionera/FChoferes.html',ctx, context_instance = RequestContext(request))


def formCamion(request):
	if request.method =='POST':
		formulario = camionForm(request.POST, request.FILES)
		if formulario.is_valid():
			capacidad = formulario.cleaned_data['capacidad']
			clase = formulario.cleaned_data['clase']
			matricula = formulario.cleaned_data['matricula']
			imagen =  formulario.cleaned_data['imagen']
			p = camion()
			p.capacidad = capacidad
			p.clase = clase
			p.matricula = matricula
			if imagen:
				p.imagen = imagen
			p.save()
			return  HttpResponseRedirect('/camiones')
		else:
			ctx =  {'formulario':formulario}
			return render_to_response('camionera/Fcamion.html',ctx,context_instance=RequestContext(request))
	else:
		formulario = camionForm()
	ctx =  {'formulario':formulario}
	return render_to_response('camionera/Fcamion.html',ctx,context_instance=RequestContext(request))

def formViaje(request):
	if request.method == 'POST':
		formulario = viajeForm(request.POST)
		if formulario.is_valid():
			ruta =formulario.cleaned_data['ruta']
			camion =formulario.cleaned_data['camion']
			chofer1 =formulario.cleaned_data['chofer1']
			asistente =formulario.cleaned_data['asistente']
			fechaSalida =formulario.cleaned_data['fechaSalida']
			p = viaje()
			p.ruta = ruta 
			p.camion = camion
			p.chofer1 = chofer1
			p.asistente = asistente
			p.contados = 0
			p.fechaSalida = fechaSalida
			p.status = True
			p.save()
			return HttpResponseRedirect('/viajesDisponibles')
		else:
			ctx = {'formulario':formulario}
			return render_to_response('camionera/Fviajes.html',ctx, context_instance=RequestContext(request))
	else:
		formulario = viajeForm()
	ctx = {'formulario':formulario}
	return render_to_response('camionera/Fviajes.html',ctx, context_instance=RequestContext(request))

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(clave__icontains=query) 
        )
        results = reservacion.objects.filter(qset)
    else:
        results = []
    return render_to_response("camionera/search.html", {
        "results": results,
        "query": query   
    },context_instance=RequestContext(request))
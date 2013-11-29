# Create your views here.
from django.http import HttpResponse
from central.apps.camionera.models import *
from django.core import serializers
from itertools import chain

def wsViajes_view(request):
	v = viaje.objects.filter(status=True)
	a1 = v[0]
	a2 = a1.ruta
	aorigen = a2.origen
	origena = aorigen.id
	ro = ciudad.objects.filter(id=origena)
	ro1 = ro[0]

	b1 = v[0]
	b2 = b1.ruta
	bdestino = b2.destino
	destinob = bdestino.id
	rd = ciudad.objects.filter(id=destinob)
	rd1 = rd[0]

	c1 = v[1]
	c2 = c1.ruta
	corigen = c2.origen
	origenc = corigen.id
	ro = ciudad.objects.filter(id=origenc)
	ro2 = ro[0]

	d1 = v[1]
	d2 = d1.ruta
	ddestino = d2.destino
	destinod = ddestino.id
	rd = ciudad.objects.filter(id=destinod)
	rd2 = rd[0]	

	e1 = v[2]
	e2 = e1.ruta
	eorigen = e2.origen
	origene = eorigen.id
	ro = ciudad.objects.filter(id=origene)
	ro3 = ro[0]

	f1 = v[2]
	f2 = f1.ruta
	fdestino = f2.destino
	destinof = fdestino.id
	rd = ciudad.objects.filter(id=destinof)
	rd3 = rd[0]	

	resultados = [ro1, rd1, ro2, rd2, ro3, rd3]

	#combined = list(chain(viaje1, viaje2))

	data = serializers.serialize("json", resultados)
	return HttpResponse(data,mimetype="application/json")
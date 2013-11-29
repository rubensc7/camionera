from django.forms import ModelForm
from django import forms
from central.apps.camionera.models import *
from django.contrib.admin import widgets  

class reservacionForm(ModelForm):
	class Meta:
		model = reservacion
		exclude =('fechaAproxSalida','status','fechaAbordar','viaje','clave')

		
class paradaForm(ModelForm):
	class Meta:
		model = viaje_parada
		
class abordarForm(forms.Form):
	class Meta:
		model = abordar

class choferForm(forms.Form):
	nombre = forms.CharField(label = "nombre", widget= forms.TextInput())
	apellidoP = forms.CharField(label = "Apellido Paterno", widget= forms.TextInput())
	apellidoM = forms.CharField(label = "Apellido Materno", widget= forms.TextInput())
	imagen = forms.ImageField(label = "fotografia", required=True)

class camionForm(forms.Form):
	matricula = forms.CharField(label='Matricula', widget=forms.TextInput())
	capacidad =  forms.IntegerField(min_value=1,label='capacidad', widget=forms.TextInput())
	clase = forms.CharField(label='clase', widget=forms.TextInput())
	imagen = forms.ImageField(label = "Imagen", required=True)

class viajeForm(forms.Form):
	ruta   = forms.ModelChoiceField(queryset = ruta.objects.all())
	camion  = forms.ModelChoiceField(queryset = camion.objects.all())
	chofer1 = forms.ModelChoiceField(label = 'Chofer', queryset = chofer.objects.all())
	asistente = forms.ModelChoiceField(label='Asistente del chofer', queryset=chofer.objects.all())
	fechaSalida = forms.DateTimeField(widget= widgets.AdminDateWidget())


'''
viaje = viaje.objects.filter(id=)
class reservacionesForm(forms.Form):
	viaje = forms.ModelChoiceField(queryset=viaje.objects.filter(status=True))
	origen =  forms.ModelChoiceField(queryset=ruta_parada.objects.all())
	destino = forms.ModelChoiceField(queryset=)
	asiento froms.ModelChoiceField(queryset=asiento.objects.all())
	nombre = forms.CharField(widget=forms.TextInput())
	apellidos = forms.CharField(widget=forms.TextInput())
'''
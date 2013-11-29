from django.conf.urls import patterns, include, url
from central.apps.camionera.views import *

urlpatterns = patterns('central.apps.camionera.views',
	#views
    url(r'^ciudades/', 'ciudadesView'),
	url(r'^viajesDisponibles/','viajesView'),
	#formularios
	url(r'^parada/','formParada'),
	url(r'^abordar/','formAbordar'),
	url(r'^reservarViaje/(?P<id>.*)/$','formReservacion'),
	url(r'^consultarViaje/(?P<id>.*)/$','consultaDatosViaje'),
	url(r'^confirmarReservacion/(?P<id>.*)/$','formAbordar'),
	url(r'^altaChofer/','formChofer'),
	url(r'^choferes/','choferesView'),
	url(r'^altaCamion/','formCamion'),
	url(r'^camiones/','camionesView'),
	url(r'^altaViaje/','formViaje'),
	url(r'^historialViajes/','historialViajes'),
	url(r'^reservaciones/','reservacionesView'),
	url(r'^search/$', 'search'),

)

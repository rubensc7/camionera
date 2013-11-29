from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('central.apps.webServices.wsViajes.views',
	url(r'^ws/viajes/$','wsViajes_view', name="ws_viajes_view"),
)
from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'central.views.home', name='home'),
    # url(r'^central/', include('central.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #urls de app camionera
    url(r'^', include('central.apps.camionera.urls')),
    #media
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    #incluir urls de webServices
    url(r'^',include('central.apps.webServices.wsViajes.urls')),
    #Inicio
    url(r'^$', 'central.apps.home.views.Inicio'),


)

from django.contrib import admin
from central.apps.camionera.models import *

admin.site.register(estado)
admin.site.register(ciudad)
admin.site.register(chofer)
admin.site.register(camion)
admin.site.register(ruta)
admin.site.register(ruta_parada)
admin.site.register(viaje)
admin.site.register(viaje_parada)
admin.site.register(reservacion)
admin.site.register(abordar)



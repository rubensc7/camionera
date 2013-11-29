from django.db import models

# Create your models here.

class estado(models.Model):
	nombre = models.CharField(max_length = 24)

	def __unicode__(self):
		return self.nombre

class ciudad(models.Model):

	def url(self,filename):
		ruta = "upload/ciudad/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre = models.CharField(max_length=24)
	estado =models.ForeignKey(estado)
	imagen = models.ImageField(upload_to = url, blank=True)

	def __unicode__(self):
		return '%s' %(self.nombre)

class chofer(models.Model):
	def url(self,filename):
		ruta = "upload/chofer/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre = models.CharField(max_length=24)
	apellidoP =models.CharField(max_length=24)
	apellidoM =models.CharField(max_length=24)
	imagen = models.ImageField(upload_to = url, blank=True)
	status = models.BooleanField(default=False)

	def __unicode__(self):
		return '%s %s' %(self.nombre, self.apellidoP)

class camion(models.Model):
	def url(self,filename):
		ruta = "upload/camion/%s/%s"%(self.matricula,str(filename))
		return ruta

	matricula = models.CharField(max_length=7)
	capacidad = models.IntegerField()
	clase = models.CharField(max_length = 12)
	imagen = models.ImageField(upload_to = url, blank=True)
	#agregar numero de placas o algo no?

	def __unicode__(self):
		return '%s %s %s' %(self.matricula, self.capacidad, self.clase)

class ruta(models.Model):
	def url(self,filename):
		ruta = "upload/ruta/%s/%s"%(self.destino,str(filename))
		return ruta

	origen = models.ForeignKey(ciudad, related_name='origen')
	destino = models.ForeignKey(ciudad, related_name='destino')
	imagen = models.ImageField(upload_to = url,blank=True)

	def __unicode__(self):
		return '%s %s' %( self.origen, self.destino)

class ruta_parada(models.Model):
	ruta = models.ForeignKey(ruta)
	numeroParada = models.IntegerField()
	parada = models.ForeignKey(ciudad)
	tiempoAprox = models.TimeField()

	def __unicode__(self):
		return '%s %s %s %s' %(self.ruta, self.numeroParada,self.parada, self.tiempoAprox)


class viaje(models.Model):
	ruta = models.ForeignKey(ruta)
	camion = models.ForeignKey(camion)
	chofer1 = models.ForeignKey(chofer, related_name='chofer1')
	asistente= models.ForeignKey(chofer, related_name='asistente')
	fechaSalida = models.DateTimeField()
	contados = models.IntegerField()
	status = models.BooleanField(default=True)

	class Meta:
		ordering = ["fechaSalida"]

	def __unicode__(self):
		return '%s' %(self.ruta)


class viaje_parada(models.Model):
	viaje = models.ForeignKey(viaje)
	rutaParada = models.ForeignKey(ruta_parada)
	fechaYHoraEntrada = models.DateTimeField()
	fechaYHoraSalida = models.DateTimeField()

	def __unicode__(self):
		return '%s %s' %(self.viaje, self.rutaParada)
'''
class asiento(models.Model):
	numero = models.IntegerField()
	camion = models.ForeignKey(camion)
	estado = models.BooleanField(default=False)

	def __unicode__(self):
		return '%s %s %s' %(self.numero, self.camion,self.estado)
'''

class reservacion(models.Model):
	clave = models.CharField(max_length=20)
	viaje = models.ForeignKey(viaje)
	#origen = models.ForeignKey(ciudad,related_name='orig')
	#destino = models.ForeignKey(ciudad,related_name='dest')
	#asiento = models.ForeignKey(asiento) # en duda lo de poner asientos
	nombre = models.CharField(max_length=48)
	apellidos = models.CharField(max_length=48)
	fechaReservacion = models.DateTimeField(auto_now=True)
	#fechaAproxSalida = models.DateTimeField()
	status = models.BooleanField(default = False)
	fechaAbordar = models.DateTimeField()
	
	def __unicode__(self):
		return '%s %s %s %s' %(self.viaje,self.nombre,self.apellidos, self.status)
 
class abordar(models.Model):
	reservacion = models.ForeignKey(reservacion)
	status = models.BooleanField(default = False)

	def __unicode__(self):
		return '%s %s' %(self.reservacion, self.status)



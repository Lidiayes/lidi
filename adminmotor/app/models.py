from django.db import models
from django.contrib.auth.models  import User

# Create your models here.

class Pais(models.Model):
	nombre_pais=models.CharField(('Nombre'),max_length=140)
	lat=models.FloatField(max_length= 120)
	lon=models.FloatField(max_length=120)
	cod_tel= models.CharField(max_length=5)
	def __unicode__(self):
		return self.nombre_pais

class Tipo_Usuario(models.Model):
	nombre_tu=models.CharField(max_length =50)
	def __unicode__(self):
		return self.nombre_tu

class Paquete(models.Model):
	tipo_paquete = models.CharField(max_length=50)
	def __unicode__(self):
		return self.tipo_paquete

class Estado (models.Model):
	nombre_estado = models.CharField(('Nombre'), max_length= 150)
	late=models.FloatField()
	lone=models.FloatField()
	pais = models.ForeignKey(Pais,verbose_name=('Pais'))
	def __unicode__(self):
		return self.nombre_estado

class Ciudad(models.Model):
	nombre_ciudad = models.CharField(('Nombre'), max_length =150)
	latc=models.FloatField()
	lonc=models.FloatField()
	pais = models.ForeignKey(Pais,verbose_name=('Pais'))
	estadoc = models.ForeignKey(Estado, verbose_name= ('Estado'))
	def __unicode__(self):
		return self.nombre_ciudad

class Modelo(models.Model):
	nombre_modelo = models.CharField(max_length =80)
	#imagen = models.ImagenField()
	def __unicode__(self):
		return self.nombre_modelo

class Marca(models.Model):
	nombre_marca = models.CharField(max_length = 80)
	modelom = models.ForeignKey(Modelo)
	def __unicode__(self):
		return self.nombre_marca

class Vehiculo(models.Model):
	placas = models.CharField(max_length = 9)
	color = models.CharField( max_length = 120)
	ano = models.DateField()
	numero_serie = models.CharField(max_length=16)
	#marca =models.ForeignKey(Marca)
	modelo = models.ForeignKey(Modelo)
	def __unicode__(self):
		return "%s-%s-%s"%(self.modelo,self.color,self.placas)

class Proveedores(models.Model):
	nombre_proveedor = models.CharField(max_length =50)
	direccion_proveedor = models.CharField(max_length =50)
	telefono_proveedor = models.CharField(max_length = 50)

class Tipo_Servicio(models.Model):
	nombre_ts = models.CharField(max_length = 100)
	vehiculo= models.ForeignKey(Vehiculo)

class Marca_producto(models.Model):
	nombre_marca_producto = models.CharField(max_length = 80)
 	def __unicode__(self):
		return self.nombre_marca_producto
		
class Tipo_pago(models.Model):
	nombre_pago =models.CharField(max_length=140)																	
	
class Compra(models.Model):
   	nombre_productoc = models.CharField(max_length=50)
	fecha = models.DateField()
	cantidad = models.IntegerField(max_length = 4)
	proveedor = models.ForeignKey(Proveedores)

class Clientes(models.Model):
	user= models.ForeignKey(User,unique=True)
	telefono_cliente = models.CharField(max_length =140)
	estadoc =models.ForeignKey(Estado)
	vehiculoc = models.ForeignKey(Vehiculo)
	#tipo_pagoc = models.ForeignKey(Tipo_pago) los tipos de pago van en ventas o compras
	#citasc = models.ForeignKey(Citas) las citas tienen un cliente
										
class Citas(models.Model):
	dia_hora = models.DateField()
	clientes= models.ForeignKey(Clientes)

class Venta(models.Model):
	cantidad= models.IntegerField(max_length = 4)
	nombre_productov = models.CharField(max_length = 20)
	clientes= models.ForeignKey(Clientes)

class Producto(models.Model):
	nombre_producto =models.CharField(max_length=50)
	cantidad_existencia =models.IntegerField(max_length=4)
	ventap= models.ForeignKey(Venta)
	comprap = models.ForeignKey(Compra)
	marcap = models.ForeignKey(Marca_producto)
						

class Usuario(models.Model):
	user = models.ForeignKey(User, unique=True)	
   	direccion_u = models.CharField(max_length =140)
	email_usuario = models.CharField(max_length =50)
	tipo_usuariou = models.ForeignKey(Tipo_Usuario)		
	paquete =models.ForeignKey(Paquete)

class Empleado(models.Model):
	user = models.ForeignKey(User,unique=True)
	direccion_emp = models.CharField(max_length=140)
	telefono_emp = models.CharField(max_length = 140)
	usuarioe = models.ForeignKey(Usuario)

class Servicio(models.Model):
	nombre_servicio = models.CharField(max_length=100)
	descripcion = models.TextField(max_length =500)
	tipo_servicio = models.ForeignKey(Tipo_Servicio)
	#vehiculo = models.ForeignKey(Vehiculo)

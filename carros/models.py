from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=30)
    matricula = models.CharField(max_length=8, default='0000',unique=True)
    anio = models.IntegerField()
    precio_por_dia = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.IntegerField(default=0)
    estado = models.CharField(max_length=10, default='3')

class Clientes(models.Model):
    nombre = models.CharField()
    apellidos = models.CharField()
    direccion = models.CharField()
    telefono = models.CharField(max_length=10, default='0000')
    no_licencia = models.CharField(max_length=10, default='0000', unique=True)
    
class Reservaciones(models.Model):
    matricula = models.ForeignKey(Auto, on_delete=models.CASCADE,default='0000')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE,default='1')
    salida = models.DateField()  # Cambiar a DateField o DateTimeField según necesidad
    entrada = models.DateField(null=True, blank=True)
    
    

from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=30)
    matricula = models.CharField(max_length=8, default='0000')
    anio = models.IntegerField()
    precio_por_dia = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.IntegerField(default=0)
    estado = models.IntegerField(max_length=5, default='3')

class clientes(models.Model):
    Nombre = models.CharField()
    apellidos = models.CharField()
    Direcion = models.CharField()
    telefono = models.CharField()
    No_licencia = models.CharField()
    
class reservaciones(models.Model):
    matricula = models.CharField()
    clientes = models.CharField()
    salida = models.CharField()
    entradas = models.CharField()
    
    

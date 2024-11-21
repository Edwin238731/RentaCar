from django.db import models

class Clientes(models.Model):
    nombre = models.CharField()
    apellidos = models.CharField()
    direccion = models.CharField()
    telefono = models.CharField(max_length=10, default='0000')
    no_licencia = models.CharField(max_length=10, default='0000', unique=True)
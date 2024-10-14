from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=30)
    anio = models.IntegerField()
    precio_por_dia = models.DecimalField(max_digits=4, decimal_places=2)
    disponible = models.BooleanField(default=True)



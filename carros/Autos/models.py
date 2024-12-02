from django.db import models

# Create your models here.
class Auto(models.Model):
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=30)
    matricula = models.CharField(max_length=8, default='0000',unique=True)
    anio = models.IntegerField()
    precio_por_dia = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.IntegerField(default=0)
    estado = models.CharField(max_length=10, default='3')
    
    def __str__(self):
        return self.title
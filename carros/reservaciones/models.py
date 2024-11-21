from django.db import models
from carros.clientesApp.models import Clientes
from carros.Autos.models import Auto


# Create your models here.
class reservacion(models.Model):
    matricula = models.ForeignKey(Auto, on_delete=models.CASCADE,default='0000')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE,default='1')
    salida = models.DateField()  # Cambiar a DateField o DateTimeField según necesidad
    entrada = models.DateField(null=True, blank=True)
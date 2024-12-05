from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=10, default='0000')
    apellidos = models.CharField(max_length=10, default='0000')
    direccion = models.CharField(max_length=10, default='0000')
    telefono = models.CharField(max_length=10, default='0000')
    no_licencia = models.CharField(max_length=10, default='0000', unique=True)
    
    def __str__(self):
        # Por ejemplo, retorna el nombre completo del cliente
        return f"{self.nombre} {self.apellidos}"

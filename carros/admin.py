from django.contrib import admin

# Register your models here.
from carros.models import Auto,clientes,reservaciones

admin.site.register(Auto)
admin.site.register(clientes)
admin.site.register(reservaciones)
from django.contrib import admin

# Register your models here.
from clientesApp.models import Auto,Clientes,Reservaciones

admin.site.register(Auto)
admin.site.register(Clientes)
admin.site.register(Reservaciones)
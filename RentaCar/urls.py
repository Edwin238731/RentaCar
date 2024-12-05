from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Importar redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('carros.clientesApp.urls')),
    path('reservar_auto/', include('carros.reservaciones.urls')),
    path('ver/', include('carros.Autos.urls')),
    path('modificar/', include('carros.cambios.urls')),
    path('reservaciones/', include('carros.reservaciones.urls')),
    path('autos/', include('carros.Autos.urls')),
    path('', lambda request: redirect('autos/', permanent=False)),  # Redirección a "autos/"
]


from django.urls import path
from .views import list_carros, form_1, clientes, reservaciones

urlpatterns = [
    path('', list_carros),
    path('clientes/', clientes),
    path('reservaciones/', reservaciones),
    path('new/', form_1,name='form_1')
]

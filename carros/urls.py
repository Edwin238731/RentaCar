from django.urls import path
from .views import list_carros, form_1, clientes, reservaciones, modificar, ver

urlpatterns = [
    path('', list_carros),
    path('clientes/', clientes),
    path('reservaciones/<int:id>/<str:matricula>/', reservaciones,name='reservar_auto'),
    path('alta/', form_1,name='form_1'),
    path('modificar/<int:id>/', modificar, name='modificar_auto'),
    path('ver/<int:id>/<str:matricula>/', ver, name='ver_auto'),
]

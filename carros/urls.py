from django.urls import path
from .views import list_carros, form_1, form_clientes, lista_clientes, lista_reservaciones, modificar, ver,reservar_auto

urlpatterns = [
    #hojas de html
    path('', list_carros, name='list_carros'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('reservaciones/',lista_reservaciones, name= 'lista_reservaciones'),
    #botones de acciones
    path('reservar_auto/<int:id>/', reservar_auto,name='reservar_auto'),
    path('modificar/<int:id>/', modificar, name='modificar_auto'),
    path('ver/<int:id>/', ver, name='ver_auto'),
    #formularios
    path('altaclientes/',form_clientes, name= 'form_2'),
    path('alta_vehiculo/', form_1,name='form_1'),
]

from django.urls import path
from .views import list_carros, lista_clientes, lista_reservaciones, modificar, ver,reservar_auto, ClientesListCreateView, ClientesDetailView

urlpatterns = [
    #hojas de html
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('reservaciones/',lista_reservaciones, name= 'lista_reservaciones'),
    #botones de acciones
    path('reservar_auto/<int:id>/', reservar_auto,name='reservar_auto'),
    path('modificar/<int:id>/', modificar, name='modificar_auto'),
    path('ver/<int:id>/', ver, name='ver_auto'),
    #formularios
    path('clientes/alta/',lista_clientes, name= 'form_2'),
    path('vehiculo/alta/', list_carros,name='form_1'),
    path('', list_carros, name='list_carros'),
    path('api/', ClientesListCreateView.as_view(), name='Clientes-list'),
    path('api/<int:pk>/', ClientesDetailView.as_view(), name='Clientes-detail'),
]

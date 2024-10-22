from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto, Clientes, Reservaciones

# Create your views here.
def list_carros(request):
    autos = Auto.objects.all()  # Consulta todos los autos
    return render(request, 'list_carros.html', {'autos': autos})

def lista_clientes(request):
    clientes_list = Clientes.objects.all()  # Consulta todos los clientes
    return render(request, 'clientes.html', {'clientes': clientes_list})

def lista_reservaciones(request):# Consulta todas las reservaciones
    reservaciones_list = Reservaciones.objects.all()
    return render(request, 'reservaciones.html', {'reservaciones': reservaciones_list})

def modificar(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'modificar.html', {'auto': auto})

def reservar_auto(request, id):#formulario para reservaciones
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'reservar_auto.html', {'auto': auto})

def ver(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'ver.html', {'auto': auto})


def form_1(request):
    auto = Auto (marca=request.POST['marca'],
    modelo=request.POST['modelo'],
    anio=request.POST['anio'],
    precio_por_dia=request.POST['precio_por_dia'],
    matricula=request.POST['matricula'],
    disponible=request.POST['disponible'],
    estado=request.POST['estado'])
    auto.save()
    return redirect('/carros/')

def form_clientes(request):
    cliente = Clientes (Nombre=request.POST['Nombre'],
    apellidos=request.POST['apellidos'],
    direcion=request.POST['direccion'],
    telefono=request.POST['telefono'],
    no_licencia=request.POST['no_licencia'])
    cliente.save()
    return redirect('/clientes/')





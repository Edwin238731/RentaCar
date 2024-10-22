from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto

# Create your views here.
def list_carros(request):
    autos = Auto.objects.all()  # Consulta todos los autos
    return render(request, 'list_carros.html', {'autos': autos})

def clientes(request):
    return render(request, 'clientes.html')

def reservaciones(request):
    return render(request, 'reservaciones.html')

def modificar(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'modificar.html', {'auto': auto})

def reservaciones(request, id, matricula):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'reservaciones.html', {'auto': auto})

def ver(request, id, matricula):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'ver.html', {'auto': auto})


def form_1(request):
    auto = Auto (marca=request.POST['marca'],modelo=request.POST['modelo'],
    anio=request.POST['anio'], precio_por_dia=request.POST['precio_por_dia'],
    disponible=request.POST['disponible'])
    auto.save()
    return redirect('/carros/')





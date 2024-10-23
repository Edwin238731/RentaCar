from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto, Clientes, Reservaciones
from django.db import IntegrityError

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
    return redirect('/autos/')

def form_clientes(request):
    error_message = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        no_licencia = request.POST.get('no_licencia')

        try:
            Clientes.objects.create(
                nombre=nombre,
                apellidos=apellidos,
                direccion=direccion,
                telefono=telefono,
                no_licencia=no_licencia
            )
            return redirect('lista_clientes')

        except IntegrityError:
            error_message = 'La licencia ya está registrada. Por favor, ingrese una licencia única.'
    return render(request, 'clientes.html', {'error': error_message})





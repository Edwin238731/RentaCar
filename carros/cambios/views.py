from django.shortcuts import render, redirect, get_object_or_404
from carros.clientesApp.models import Clientes
from carros.reservaciones.models import reservacion
from carros.Autos.models import Auto
from django.db import IntegrityError

def lista_reservaciones(request):# Consulta todas las reservaciones
    reservaciones_list = reservacion.objects.all()
    return render(request, 'reservaciones.html', {'reservaciones': reservaciones_list})

def reservar_auto(request, id):#formulario para reservaciones
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'reservar_auto.html', {'auto': auto})

def ver(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'ver.html', {'auto': auto})


def list_carros(request):
    autos = Auto.objects.all()  # Consulta todos los autos
    error_message = None

    if request.method == 'POST':
        # Manejo del formulario
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        anio = request.POST.get('anio')
        precio_por_dia = request.POST.get('precio_por_dia')
        matricula = request.POST.get('matricula')
        disponible = request.POST.get('disponible')
        estado = request.POST.get('estado')

        # Validación y guardado
        try:
            Auto.objects.create(
                marca=marca,
                modelo=modelo,
                anio=anio,
                precio_por_dia=precio_por_dia,
                matricula=matricula,
                disponible=disponible,
                estado=estado
            )
            return redirect('list_carros')

        except IntegrityError:
            error_message = 'Error al registrar el auto, matricula ya registrada'

    return render(request, 'list_carros.html', {
        'autos': autos,
        'error': error_message
    })

def lista_clientes(request):
    clientes = Clientes.objects.all()
    error_message = None

    if request.method == 'POST':
        # Manejo del formulario
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        no_licencia = request.POST.get('no_licencia')

        try:
            # Crear un nuevo cliente
            Clientes.objects.create(
                nombre=nombre, apellidos=apellidos,
                direccion=direccion, telefono=telefono,
                no_licencia=no_licencia
            )
            return redirect('lista_clientes')

        except IntegrityError:
            error_message = 'La licencia ya está registrada. Por favor, ingrese una licencia única.'

    return render(request, 'clientes.html', {
        'clientes': clientes,
        'error': error_message,
    })
    
def modificar(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.precio_por_dia = request.POST['precio_por_dia']
        auto.matricula = request.POST['matricula']
        auto.disponible = request.POST['disponible']
        auto.estado = request.POST['estado']
        auto.save()
        return redirect('list_carros')  # Redirige después de guardar

    return render(request, 'list_carros.html', {'auto': auto})
from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Libro, Prestamo, Lector
from datetime import datetime, timedelta

# Create your views here.

from .models import Lector
from .models import Libro
from django.db.models import Q  # Importar Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    return render(request,"home.html",context={"current_tab":"home"})

def lectores(request):
    return render(request,"lectores.html",context={"current_tab":"lectores"})

def reservaciones(request):
    return HttpResponse("SOLICITUD EJEMPLARES")

def save_usuario(request):
    nombre_usuario = request.POST['nombre_usuario']
    return render(request,"welcome.html",context={'nombre_usuario':nombre_usuario})

def lectores_tab(request):
    query = request.GET.get('query', '')
    lista_lectores = Lector.objects.filter(  # Cambiado a Lector (singular)
        Q(matricula__icontains=query) | Q(nombre__icontains=query) | Q(curso__icontains=query)
    )
    return render(request, "lectores.html", {"current_tab": "lectores", "lectores": lista_lectores, "query": query})

def save_lector(request):
    lector_item = Lector(  # Cambiado a Lector (singular)
        matricula=request.POST['matricula'],
        nombre=request.POST['nombre'],  # Cambiado a 'nombre'
        curso=request.POST['curso'],
        observaciones=request.POST['observaciones'],
        activo=True
    )
    lector_item.save()
    return redirect('lectores')  # Redirigir a la lista de lectores

def libros_disponibles(request):
    query_titulo = request.GET.get('titulo', '')
    query_autor = request.GET.get('autor', '')
    query_genero = request.GET.get('genero', '')

    libros = Libro.objects.filter(cantidad_disponible__gt=0)

    if query_titulo:
        libros = libros.filter(titulo__icontains=query_titulo)
    if query_autor:
        libros = libros.filter(autor__icontains=query_autor)
    if query_genero:
        libros = libros.filter(genero__icontains=query_genero)

    return render(request, 'libros.html', {'libros': libros})

def prestamo_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    usuario = request.user

    if request.method == 'POST':
        if libro.cantidad_disponible > 0:  # <-- If statement starts here
            prestamo = Prestamo(
                libro=libro,
                usuario=usuario,
                fecha_prestamo=datetime.now(),
                fecha_devolucion=datetime.now() + timedelta(days=7)
            )
            prestamo.save()
            libro.cantidad_disponible -= 1
            libro.save()
            return redirect('confirmacion_prestamo') 
        else:
            return render(request, 'libros.html', {'libros': Libro.objects.all(), 'error': 'Libro no disponible'})
    else:
        return render(request, 'prestamo_libro.html', {'libro': libro})
    
@login_required
def mochila(request):
    if hasattr(request.user, 'lector'):  # Check if user is Lector
        prestamos = Prestamo.objects.filter(lector=request.user.lector, devuelto=False)
        return render(request, 'mochila.html', {'prestamos': prestamos})
    else:
        return render(request, 'mochila.html', {'error': 'Solo los lectores pueden ver la mochila.'})
    
def devoluciones(request):
    if request.method == 'POST':
        prestamo_id = request.POST['prestamo_id']
        try:
            prestamo = Prestamo.objects.get(pk=prestamo_id)
            prestamo.devuelto = True
            prestamo.fecha_devolucion = datetime.now()
            prestamo.save()

            # Aumentar la cantidad disponible del libro
            prestamo.libro.cantidad_disponible += 1
            prestamo.libro.save()

            # Opcional: agregar un mensaje de éxito
            messages.success(request, 'Devolución registrada exitosamente.')
        except Prestamo.DoesNotExist:
            # Opcional: agregar un mensaje de error
            messages.error(request, 'No se encontró el préstamo con el ID proporcionado.')

    # Obtener todos los préstamos no devueltos para mostrarlos en la plantilla
    prestamos_no_devueltos = Prestamo.objects.filter(devuelto=False)
    return render(request, 'devoluciones.html', {'prestamos_no_devueltos': prestamos_no_devueltos})

@login_required
@permission_required('sistema_biblioteca_app.add_prestamo', raise_exception=True) # Requiere permiso para crear prestamos
def registrar_prestamo(request):
    if request.method == 'POST':
        lector_id = request.POST['lector_id']
        libro_id = request.POST['libro_id']
        try:
            lector = Lector.objects.get(pk=lector_id)
            libro = Libro.objects.get(pk=libro_id)
            prestamo = Prestamo(
                lector=lector,
                libro=libro,
                fecha_prestamo=datetime.now(),
                fecha_devolucion=datetime.now() + timedelta(days=14)  # Préstamo por 14 días (puedes ajustar)
            )
            prestamo.save()
            messages.success(request, 'Préstamo registrado exitosamente.')
            return redirect('libros')  # Redirige a la lista de libros después de registrar el préstamo
        except (Lector.DoesNotExist, Libro.DoesNotExist):
            messages.error(request, 'Lector o libro no encontrado.')

    lectores = Lector.objects.all()
    libros = Libro.objects.all()
    return render(request, 'registrar_prestamo.html', {'lectores': lectores, 'libros': libros})


@login_required
@permission_required('sistema_biblioteca_app.change_prestamo', raise_exception=True) # Requiere permiso para modificar prestamos
def registrar_devolucion(request):
    if request.method == 'POST':
        prestamo_id = request.POST['prestamo_id']
        try:
            prestamo = Prestamo.objects.get(pk=prestamo_id)
            prestamo.devuelto = True
            prestamo.fecha_devolucion = datetime.now()
            prestamo.save()

            # Aumentar la cantidad disponible del libro
            prestamo.libro.cantidad_disponible += 1
            prestamo.libro.save()

            messages.success(request, 'Devolución registrada exitosamente.')
        except Prestamo.DoesNotExist:
            messages.error(request, 'Préstamo no encontrado.')

    prestamos = Prestamo.objects.filter(devuelto=False)
    return render(request, 'registrar_devolucion.html', {'prestamos': prestamos})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'detalle_libro.html', {'libro': libro})

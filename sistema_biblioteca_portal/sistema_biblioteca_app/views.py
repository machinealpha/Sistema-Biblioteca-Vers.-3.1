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
    query = request.GET.get('query', '')
    libros = Libro.objects.filter(cantidad_disponible__gt=0)

    if query:
        libros = libros.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query) | Q(genero__icontains=query)
        )

    return render(request, 'libros.html', {
        'libros': libros,
        'query': query,
        'current_tab': 'libros'
    })
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
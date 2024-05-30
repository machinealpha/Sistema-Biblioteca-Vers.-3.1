from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.

from .models import Lectores
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
    query = request.GET.get('query', '')  # Obtiene el término de búsqueda de la URL
    lista_lectores = Lectores.objects.filter(
        Q(matricula__icontains=query) | Q(lector__icontains=query) | Q(curso__icontains=query)
    )  # Filtra por matrícula, lector o curso
    return render(request, "lectores.html", {"current_tab": "lectores", "lectores": lista_lectores, "query": query})

def save_lector(request):
    lector_item = Lectores(
        matricula=request.POST['matricula'],
        lector=request.POST['lector'],  # Asumiendo que 'lector' es un campo en el modelo Lectores
        curso=request.POST['curso'],
        observaciones=request.POST['observaciones'],
        active=True
    )
    lector_item.save()
    return redirect('lectores')

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
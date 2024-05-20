from django.shortcuts import render
#from django.contrib import render
from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    return render(request,"index.html",context={})

def reservaciones(request):
    return HttpResponse("SOLICITUD EJEMPLARES")

def save_usuario(request):
    nombre_usuario = request.POST['nombre_usuario']
    return render(request,"welcome.html",context={'nombre_usuario':nombre_usuario})
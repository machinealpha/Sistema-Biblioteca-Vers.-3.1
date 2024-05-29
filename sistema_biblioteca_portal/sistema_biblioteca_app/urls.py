"""
URL configuration for sistema_biblioteca_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, save_usuario, save_lector, lectores_tab, reservaciones  # Importamos todas las vistas necesarias

urlpatterns = [
    path('', home),
    path('home', home),
    path('lectores', lectores_tab, name='lectores'),  # Redirigimos a lectores_tab
    path('save', save_usuario),
    path('lectores/add', save_lector, name='save_lector'),
    path('reservaciones', reservaciones),  # Asegúrate de tener la vista reservaciones definida
]
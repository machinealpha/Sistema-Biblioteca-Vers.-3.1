from django.contrib import admin
from django.urls import path
from .views import home, save_usuario, save_lector, lectores_tab, reservaciones, libros_disponibles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home', home),
    path('lectores', lectores_tab, name='lectores'),
    path('save', save_usuario),
    path('lectores/add', save_lector, name='save_lector'),
    path('reservaciones', reservaciones),
    path('libros/', libros_disponibles, name='libros'),
]
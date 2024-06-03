from django.contrib import admin
from django.urls import path
from .views import home, save_usuario, save_lector, lectores_tab, reservaciones, libros_disponibles, prestamo_libro, mochila, devoluciones, detalle_libro
from django.contrib.auth import views as auth_views
from .views import registrar_prestamo, registrar_devolucion, register, login_view, ConfirmacionPrestamoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home', home),
    path('lectores', lectores_tab, name='lectores'),
    path('save', save_usuario),
    path('lectores/add', save_lector, name='save_lector'),
    path('reservaciones', reservaciones),
    path('libros/', libros_disponibles, name='libros'),
    path('prestamo/<int:libro_id>/', prestamo_libro, name='prestamo_libro'),
    path('mochila/', mochila, name='mochila'),
    path('devoluciones/', devoluciones, name='devoluciones'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('prestamo/registrar/', registrar_prestamo, name='registrar_prestamo'),
    path('devolucion/registrar/', registrar_devolucion, name='registrar_devolucion'),
    path('libro/<int:libro_id>/', detalle_libro, name='detalle_libro'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('prestamo/<int:libro_id>/confirmar/', ConfirmacionPrestamoView.as_view(), name='confirmacion_prestamo'),


]
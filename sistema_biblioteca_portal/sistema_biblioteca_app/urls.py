from django.contrib import admin
from django.urls import path, include  # Importa include para agrupar URLs

from sistema_biblioteca_app.views import (
    home, save_usuario, save_lector, lectores_tab, 
    reservaciones, libros_disponibles, prestamo_libro, 
    mochila, devoluciones, detalle_libro, register, 
    ConfirmacionPrestamoView
)
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('home', home, name='home'),
    path('lectores/', lectores_tab, name='lectores'),
    # path('save', save_usuario),  # Esta ruta no parece estar siendo utilizada
    path('lectores/add', save_lector, name='save_lector'),
    path('reservaciones', reservaciones),
    path('libros/', libros_disponibles, name='libros'),
    path('prestamo/<int:libro_id>/', prestamo_libro, name='prestamo_libro'),
    path('mochila/', mochila, name='mochila'),
    path('devoluciones/', devoluciones, name='devoluciones'),
    path('libro/<int:libro_id>/', detalle_libro, name='detalle_libro'),
    path('register/', register, name='register'),
    
    # Agrupamos las URLs de autenticación
    path('accounts/', include([
        path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ])),

    path('prestamo/<int:libro_id>/confirmar/', ConfirmacionPrestamoView.as_view(), name='confirmacion_prestamo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

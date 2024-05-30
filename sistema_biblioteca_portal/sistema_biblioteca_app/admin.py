from django.contrib import admin
from .models import Lector
from .models import Prestamo 
from .models import Libro

# Register your models here.
admin.site.register(Lector)
admin.site.register(Libro)
admin.site.register(Prestamo)
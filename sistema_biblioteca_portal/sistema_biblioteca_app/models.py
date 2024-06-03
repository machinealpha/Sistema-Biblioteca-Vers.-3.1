from django.db import models
from django.contrib.auth.models import User

class Lector(models.Model):  # Cambiamos el nombre a "Lector" (singular)
    matricula = models.CharField(max_length=200, unique=True)  # Matrícula única
    nombre = models.CharField(max_length=200)  # Cambiamos 'lector' por 'nombre'
    curso = models.CharField(max_length=200, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)  # Opcional
    activo = models.BooleanField(default=True)  # Cambiamos 'active' por 'activo'

    def __str__(self):
        return f"{self.matricula} - {self.nombre}"  # Representación más informativa

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    editorial = models.CharField(max_length=100)
    año_publicacion = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    cantidad_disponible = models.PositiveIntegerField(default=1)
    imagen = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):  # Nuevo modelo para registrar préstamos
    lector = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.lector} - {self.libro} ({self.fecha_prestamo})"

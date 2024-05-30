from django.db import models

# Create your models here.
class Lectores(models.Model):
    def __str__(self):
        return self.lector
    matricula=models.CharField(max_length=200)
    lector=models.CharField(max_length=200)
    curso=models.CharField(max_length=200)
    observaciones=models.TextField()
    active=models.BooleanField(default=True)


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN de 13 dígitos, único
    editorial = models.CharField(max_length=100)
    año_publicacion = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)  # Campo para el género del libro
    cantidad_disponible = models.PositiveIntegerField(default=1)
    imagen = models.ImageField(upload_to='portadas/', null=True, blank=True)  # Para almacenar la imagen de portada

    def __str__(self):
        return self.titulo
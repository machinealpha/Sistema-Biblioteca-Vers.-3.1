from django.db import models

# Create your models here.
class lectores(models.Model):
    matricula=models.CharField(max_length=200)
    nombre=models.CharField(max_length=200)
    curso=models.CharField(max_length=200)
    observaciones=models.TextField()
    active=models.BooleanField(default=True)
from django.db import models

# Create your models here.
class lectores(models.Model):
    def __str__(self):
        return self.lector
    matricula=models.CharField(max_length=200)
    lector=models.CharField(max_length=200)
    curso=models.CharField(max_length=200)
    observaciones=models.TextField()
    active=models.BooleanField(default=True)
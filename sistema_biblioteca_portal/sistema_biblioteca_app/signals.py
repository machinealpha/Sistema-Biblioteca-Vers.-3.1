from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Prestamo

@receiver(post_delete, sender=Prestamo)
def actualizar_cantidad_libro(sender, instance, **kwargs):
    instance.libro.cantidad_disponible += 1  # Aumentar la cantidad disponible
    instance.libro.save()
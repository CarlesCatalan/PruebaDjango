from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    completada_por = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

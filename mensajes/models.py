from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):
    name = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"

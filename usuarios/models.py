from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

    @property
    def foto_url(self):
        if self.foto:
            return self.foto.url
        return None

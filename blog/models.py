from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    completada_por = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    name = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"


class Encuesta(models.Model):
    contacto = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    opinion = models.CharField(max_length=200)
    satisfaccion = models.IntegerField(choices=[(1, 'Muy insatisfecho'), (
        2, 'Insatisfecho'), (3, 'Neutral'), (4, 'Satisfecho'), (5, 'Muy satisfecho')])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opinion


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

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo


class ComentarioPost(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en '{self.post.titulo}'"

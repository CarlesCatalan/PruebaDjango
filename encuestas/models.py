from django.db import models
from django.contrib.auth.models import User


class Encuesta(models.Model):
    contacto = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    opinion = models.CharField(max_length=200)
    satisfaccion = models.IntegerField(choices=[
        (1, 'Muy insatisfecho'),
        (2, 'Insatisfecho'),
        (3, 'Neutral'),
        (4, 'Satisfecho'),
        (5, 'Muy satisfecho'),
    ])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opinion

from django.contrib import admin
from .models import Encuesta, Post, Tarea, Mensaje, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Tarea)
admin.site.register(Mensaje)
admin.site.register(Encuesta)
admin.site.register(Profile)

from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.listatareas, name='tareas'),
    path('tareas/completar/<int:tarea_id>/',
         views.completartarea, name='completartarea'),
    path('tareas/crear/', views.creartarea, name='creartarea'),
    path('home/tareasdb/', views.tareas_db, name='tareas_db'),
    path('generarexcel/', views.generarexcel, name='generarexcel'),
]

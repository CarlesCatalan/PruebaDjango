from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/tareasdb/', views.tareas_db, name='tareas_db'),
    path('saludo/', views.saludo),
    path('posts/', views.listapost, name='posts'),
    path('saludoform/', views.saludoform),
    path('tareas/', views.listatareas, name='tareas'),
    path('tareas/completar/<int:tarea_id>/',
         views.completartarea, name='completartarea'),
    path('tareas/crear/', views.creartarea, name='creartarea'),
    path('mensajes/', views.mensaje, name='mensaje'),
    path('encuesta/', views.encuesta, name='encuesta'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('generarexcel/', views.generarexcel, name='generarexcel'),
    path('clima/', views.clima, name='clima'),
]

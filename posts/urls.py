from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.listapost, name='posts'),
]

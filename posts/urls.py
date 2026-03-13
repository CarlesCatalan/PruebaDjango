from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.listapost, name='posts'),
    path('posts/<int:post_id>/comentar/',
         views.comentar_post, name='comentar_post'),
]

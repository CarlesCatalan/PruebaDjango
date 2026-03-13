from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('saludo/', views.saludo, name='saludo'),
    path('saludoform/', views.saludoform, name='saludoform'),
]

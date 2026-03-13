from django.urls import path
from . import views

urlpatterns = [
    path('clima/', views.clima, name='clima'),
]

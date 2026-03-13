from django.urls import path
from . import views

urlpatterns = [
    path('ia/', views.ia_chat, name='ia_chat'),
]

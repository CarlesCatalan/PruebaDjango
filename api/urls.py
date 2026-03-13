from rest_framework.routers import DefaultRouter
from django.urls import path, include
from tareas.api_views import TareaViewSet

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('', include(router.urls)),
]

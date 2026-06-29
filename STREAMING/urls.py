from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PlaylistViewSet, TreinoViewSet, 
    RegistroExecucaoViewSet, DetalheExercicioViewSet
)

router = DefaultRouter()
router.register(r'playlists', PlaylistViewSet)
router.register(r'treinos', TreinoViewSet)
router.register(r'execucoes', RegistroExecucaoViewSet)
router.register(r'detalhes', DetalheExercicioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
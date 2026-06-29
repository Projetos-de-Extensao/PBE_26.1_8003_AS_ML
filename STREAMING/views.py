from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Playlist, Treino, RegistroExecucao, DetalheExercicio
from .serializers import (
    PlaylistSerializer, TreinoSerializer, 
    RegistroExecucaoSerializer, DetalheExercicioSerializer
)

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer

class RegistroExecucaoViewSet(viewsets.ModelViewSet):
    queryset = RegistroExecucao.objects.all()
    serializer_class = RegistroExecucaoSerializer

class DetalheExercicioViewSet(viewsets.ModelViewSet):
    queryset = DetalheExercicio.objects.all()
    serializer_class = DetalheExercicioSerializer
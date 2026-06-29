from rest_framework import serializers
from .models import Playlist, Treino, RegistroExecucao, DetalheExercicio

class DetalheExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheExercicio
        fields = '__all__'

class RegistroExecucaoSerializer(serializers.ModelSerializer):
    detalhes = DetalheExercicioSerializer(many=True, read_only=True)
    volume_total = serializers.ReadOnlyField()

    class Meta:
        model = RegistroExecucao
        fields = ['id', 'playlist', 'treino', 'data_realizacao', 'observacoes', 'volume_total', 'detalhes']

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    execucoes = RegistroExecucaoSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'usuario', 'nome', 'objetivo', 'data_criacao', 'execucoes']
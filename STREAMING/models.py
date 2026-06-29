from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    """Agrupador de sessões de treino (ex: Ciclo de Verão)"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    nome = models.CharField(max_length=100)
    objetivo = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.usuario.username}"

class Treino(models.Model):
    """Definição do plano de treino (ex: Treino A - Peito)"""
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class RegistroExecucao(models.Model):
    """Registro de uma sessão realizada dentro de uma Playlist"""
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='execucoes')
    treino = models.ForeignKey(Treino, on_delete=models.PROTECT)
    data_realizacao = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    @property
    def volume_total(self):
        """Calcula o volume total da sessão (Soma de Carga x Reps x Séries)"""
        detalhes = self.detalhes.all()
        return sum(d.carga_utilizada * d.series_feitas * d.repeticoes_feitas for d in detalhes)

    def __str__(self):
        return f"Execução {self.treino.titulo} em {self.data_realizacao.strftime('%d/%m/%Y')}"

class DetalheExercicio(models.Model):
    """Dados técnicos de cada exercício feito no registro"""
    registro = models.ForeignKey(RegistroExecucao, on_delete=models.CASCADE, related_name='detalhes')
    nome_exercicio = models.CharField(max_length=100)
    carga_utilizada = models.FloatField()
    series_feitas = models.IntegerField()
    repeticoes_feitas = models.IntegerField()

    def __str__(self):
        return f"{self.nome_exercicio} - {self.carga_utilizada}kg"
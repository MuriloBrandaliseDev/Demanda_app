# core/models.py

from django.db import models

class Demanda(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_demanda = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)  # Se já existe
    is_concluded = models.BooleanField(default=False)  # Campo para concluir a demanda

    def __str__(self):
        return self.titulo

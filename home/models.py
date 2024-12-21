from django.db import models
from django.contrib.auth.models import User

class Tarefas(models.Model):
    PRIORIDADE_CHOICES = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    ]
    STATUS_CHOICES = [
        ('AB', 'Aberta'),
        ('EP', 'Em Progresso'),
        ('CO', 'Concluída'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_vencimento = models.DateField()
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


from django.db import models
from .tarefa import Tarefa


class Material(models.Model):
    tipo = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
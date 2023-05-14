from django.db import models
from .fazenda import Fazenda

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    custo = models.IntegerField()
    categoria = models.CharField(max_length=30)
    tarefa_dependente = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE)
    feito = models.BooleanField(default=False)
    
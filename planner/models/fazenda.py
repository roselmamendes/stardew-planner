from django.db import models


class Fazenda(models.Model):
    nome = models.CharField(max_length=20, default='Sem nome')
    receita = models.IntegerField()
    gasto_previsto = models.IntegerField()
    data_receita_inicial = models.CharField(max_length=20)

    def __str__(self):
        return "Nome: " + self.nome + " / Receita: " + str(self.receita)
    
    def get_quantidade_total_materiais(self):
        quantidades = {
            "madeira": 0,
            "pedra": 0,
            "minério de ferro": 0,
            "carvão": 0
        }
        tarefas = self.tarefa_set.all()
        for tarefa in tarefas:
            materiais = tarefa.material_set.all()
            quantidades = Fazenda.soma_quantidade_total_materiais(quantidades, materiais)

        return quantidades
    
    def soma_quantidade_total_materiais(quantidades, materiais):
        for material in materiais:
            if material.tipo.lower() in quantidades:
                quantidades[material.tipo.lower()]+= material.quantidade
        return quantidades
    
    def get_gasto_previsto(self):
        tarefas = self.tarefa_set.all()
        soma = 0
        for tarefa in tarefas: 
            if not tarefa.feito:
                soma += tarefa.custo

        return soma
    
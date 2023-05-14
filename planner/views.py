from django.shortcuts import render
from .models import Fazenda

def index(request):
    context = {
        "fazendas": Fazenda.objects.all(),
    }
    return render(request, "planner/index.html", context)

def get_fazenda(request, fazenda_id):
    fazenda = Fazenda.objects.get(id=fazenda_id)
    context = {
        "tarefas": fazenda.tarefa_set.all(),
        "fazenda": fazenda,
        "gasto_previsto": fazenda.get_gasto_previsto()
    }
    return render(request, "planner/detail.html", context)

def get_materiais(request, fazenda_id):
    fazenda = Fazenda.objects.get(id=fazenda_id)
    quantidades = fazenda.get_quantidade_total_materiais()
        
    context = {
        "quantidades": quantidades,
        "fazenda_nome": fazenda.nome,
        "fazenda_id": fazenda.id
    }
    return render(request, "planner/materiais.html", context)
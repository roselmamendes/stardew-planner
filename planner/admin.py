from django.contrib import admin

from .models import Fazenda, Tarefa, Material

# Register your models here.
admin.site.register(Fazenda)
admin.site.register(Tarefa)
admin.site.register(Material)
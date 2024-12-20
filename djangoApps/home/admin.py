from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Tarefas)
class Tarefas(admin.ModelAdmin):
    list_display=('titulo' , 'descricao' , 'data_vencimento' , 'prioridade' , 'status' , 'usuario')
    list_filter=('titulo',)


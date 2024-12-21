from django.shortcuts import render,get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from .forms import *
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    tarefas= Tarefas.objects.filter(usuario=request.user).order_by('data_vencimento')
    return render(request,'home/pages/index.html',{'tarefas':tarefas})

def login_view(request):
    form = AuthenticationForm(request)
    form_action=reverse('home:login')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home:index')
        
    context = {
        'form': form,
        'form_action': form_action
    }
    return render(request,'home/pages/login.html',context)

def criarconta(request):
    form_action = reverse('home:criarconta')

    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco.
            # Você pode redirecionar ou enviar uma mensagem de sucesso aqui.
            return redirect('home:index')  # Exemplo de redirecionamento após o cadastro.

    else:
        form = RegisterUser()  # Cria um formulário vazio para exibir no método GET.

    context = {
        'form': form,
        'form_action': form_action
    }
    return render(request,'home/pages/criarconta.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect ('home:index')



@login_required
def adicionar_tarefa(request):
    form_action=reverse('home:criartarefa')
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user  # Associa a tarefa ao usuário autenticado
            tarefa.save()
            return redirect('home:index')  # Redireciona após adicionar
    else:
        form = TarefaForm()
    context={
        'form':form,
        'form_action':form_action
    }
    
    return render(request, 'home/pages/criando_tarefas.html', context)

@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id, usuario=request.user)

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('home:index')  # Redireciona para a página principal ou onde desejar
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'home/pages/editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def apagar_tarefa(request,tarefa_id):
    tarefa=get_object_or_404(Tarefas ,id=tarefa_id)
    
    if request.method=='POST':
        tarefa.delete()
        return redirect('home:index')
    return render(request, 'home/pages/excluir_tarefa.html', {'tarefa': tarefa})
    
    
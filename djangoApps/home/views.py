from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from .forms import *
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    return render(request,'home/pages/index.html')

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

def logout_view(request):
    logout(request)
    return redirect ('home:index')
    
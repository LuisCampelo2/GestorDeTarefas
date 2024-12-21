from django.contrib import admin
from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('criarconta/',views.criarconta,name='criarconta'),
    path('logout/', views.logout_view, name='logout'),
    path('criandoTarefa/',views.adicionar_tarefa,name='criartarefa'),
    path('editartarefa/<int:tarefa_id>/',views.editar_tarefa,name='editartarefa'),
    path('apagartarefa/<int:tarefa_id>/',views.apagar_tarefa,name='apagartarefa'),
]
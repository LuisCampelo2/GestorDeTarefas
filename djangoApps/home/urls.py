from django.contrib import admin
from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('criarconta/',views.criarconta,name='criarconta'),
    path('logout/', views.logout_view, name='logout'),
]
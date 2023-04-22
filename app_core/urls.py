from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    
    path('login/', views.login, name='login'),
    path('validar_login', views.validar_login, name='validar_login'),
    
    path('registrar/', views.registrar, name='registrar'),
    path('validar_registrar', views.validar_registrar, name='validar_registrar'),
    
    path('adicionar_renda', views.adicionar_renda, name='adicionar_renda'),
    path('ver_renda/<int:id>', views.ver_renda, name='ver_renda'),
    path('alterar_renda', views.alterar_renda, name='alterar_renda'),
    path('excluir_renda/<int:id>', views.excluir_renda, name='excluir_renda'),
    
    path('tabela', views.tabela, name='tabela'),
    path('sair/', views.sair, name = 'sair')
]
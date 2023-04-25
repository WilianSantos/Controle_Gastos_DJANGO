from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    
    path('', views.login, name='login'),
    path('validar_login', views.validar_login, name='validar_login'),
    
    path('registrar/', views.registrar, name='registrar'),
    path('validar_registrar', views.validar_registrar, name='validar_registrar'),
    
    path('adicionar_renda', views.adicionar_renda, name='adicionar_renda'),
    path('ver_renda/<int:id>', views.ver_renda, name='ver_renda'),
    path('alterar_renda', views.alterar_renda, name='alterar_renda'),
    path('excluir_renda/<int:id>', views.excluir_renda, name='excluir_renda'),
    
    path('adicionar_gasto', views.adicionar_gasto, name='adicionar_gasto'),
    path('ver_gasto/<int:id>', views.ver_gasto, name='ver_gasto'),
    path('alterar_gasto', views.alterar_gasto, name='alterar_gasto'),
    path('excluir_gasto/<int:id>', views.excluir_gasto, name='excluir_gasto'),
    
    path('tabela_renda/', views.tabela_renda, name='tabela_renda'),
    path('tabela_gasto/', views.tabela_gasto, name='tabela_gasto'),
    
    path('graficos/', views.graficos, name='graficos'),
    path('relatorio_gastos/', views.relatorio_gastos, name='relatorio_gastos'),
    path('relatorio_rendas', views.relatorio_rendas, name='relatorio_rendas'),
    
    path('sair/', views.sair, name = 'sair')
]
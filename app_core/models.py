from django.db import models

from datetime import datetime
from django.utils import timezone


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    
class Rendas(models.Model):
    renda_principal = models.FloatField()
    renda_secundaria = models.FloatField(default=0)
    data = models.DateField(default=datetime.today())
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.renda_principal)
    
    class Meta:
        verbose_name = 'Renda'
        verbose_name_plural = 'Rendas'
    
    
class Gastos(models.Model):
    gasto = models.CharField(max_length=80)
    valor = models.FloatField()
    data = models.DateField(default=datetime.today())
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.gasto
    
    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'

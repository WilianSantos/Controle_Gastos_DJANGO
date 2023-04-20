from django.db import models


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=60)
    renda = models.FloatField(null=True)
    
    def __str__(self):
        return self.nome
    
    
class Rendas(models.Model):
    renda_principal = models.FloatField()
    renda_secundaria = models.FloatField()
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.renda_principal
    
    
class Gastos(models.Model):
    gasto = models.CharField('Gasto', max_length=80)
    valor = models.FloatField()
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.gasto

from django.db import models


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email')
    senha = models.CharField(max_length=60)
    renda_total = models.FloatField(null=True, default=0)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    
class Rendas(models.Model):
    renda_principal = models.FloatField()
    renda_secundaria = models.FloatField()
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.renda_principal
    
    class Meta:
        verbose_name = 'Renda'
        verbose_name_plural = 'Rendas'
    
    
class Gastos(models.Model):
    gasto = models.CharField('Gasto', max_length=80)
    valor = models.FloatField()
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.gasto
    
    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'

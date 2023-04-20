from django.db import models


class Usuario(models.model):
    nome = models.CharField('Nome', max_length=50)
    

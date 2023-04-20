from django.contrib import admin

from .models import Usuario, Rendas, Gastos


admin.site.register(Usuario)
admin.site.register(Rendas)
admin.site.register(Gastos)

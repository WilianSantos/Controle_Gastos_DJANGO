from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    

def tabela(request):
    return render(request,
                  'tables.html'
                  )

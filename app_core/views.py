from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.formats import localize

from hashlib import sha256
from datetime import datetime

from .models import Usuario, Rendas

from .forms import AdicionarRenda


def index(request):
    if request.session.get('usuario'):
        usuario_logado = request.session.get('usuario')
        
        usuario = Usuario.objects.get(id=request.session['usuario'])
        
        rendas = Rendas.objects.filter(usuario=request.session['usuario'])
    
        renda_total = 0
        for renda in rendas:
            renda_total += renda.renda_principal
            renda_total += renda.renda_secundaria
        usuario.renda_total = renda_total
        usuario.save()
        
        form_renda = AdicionarRenda()
        form_renda.fields['usuario'].initial = request.session['usuario']
        
        contador = 0
        
        return render(request, 'index.html', {'usuario_logado': usuario_logado,
                                              'usuario': usuario,
                                              'form_renda': form_renda,
                                              'rendas': rendas,
                                              'contador': contador                                  
        })
    else:
        redirect('/login/') 
    

def tabela(request):
    return render(request,
                  'tables/tables.html'
                  )
    
    
def registrar(request):
    if request.session.get('usuario'):
        return redirect('index/')
    
    status = request.GET.get('status')
    
    return render(request, 'register/register.html', {'status': status})


def validar_registrar(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    confirma_senha = request.POST.get('confirma-senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/registrar/?status=1')

    if len(senha) < 8:
        return redirect('/registrar/?status=2')
    
    if senha != confirma_senha:
        return redirect('/registrar/?status=3')

    if len(usuario) > 0:
        return redirect('/registrar/?status=4')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,
                          senha = senha,
                          email = email)
        usuario.save()

        return redirect('/registrar/?status=0')
    except:
        return redirect('/registrar/?status=5')


def login(request):
    if request.session.get('usuario'):
        return redirect('index/')
    
    status = request.GET.get('status')
    
    return render(request, 'login/login.html', {'status': status})


def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/index/')

    return redirect('/login/')


def sair(request):
    request.session.flush()
    return redirect('/login/')


def adicionar_renda(request):
    if request.method == 'POST':
        form_renda = AdicionarRenda(request.POST)
        
        if form_renda.is_valid:
            form_renda.save()
            return redirect('/index/')
        else:
            return redirect('/index/')
        
        
def ver_renda(request, id):
    if request.session.get('usuario'):
        renda = Rendas.objects.get(id=id)
        if request.session.get('usuario') == renda.usuario.id:
            
            return render(request, 'forms/form_renda.html', {'renda': renda})
        else:
            return HttpResponse('Esta não é uma renda sua')
    return redirect('/login/?status=2')


def alterar_renda(request):
    renda_id = request.POST.get('renda_id')
    renda_principal = request.POST.get('renda_principal')
    renda_secundaria = request.POST.get('renda_secundaria')
    
    renda = Rendas.objects.get(id=renda_id)
    if renda.usuario.id == request.session['usuario']:
        
        renda.renda_principal = float(renda_principal.replace(',', '.'))
        renda.renda_secundaria = float(renda_secundaria.replace(',', '.'))
        renda.save()
        return redirect(f'/index/')
    else:
        return redirect('/login/')
    
    
def excluir_renda(request, id):
    renda = Rendas.objects.get(id=id).delete()
    return redirect(f'/index/')

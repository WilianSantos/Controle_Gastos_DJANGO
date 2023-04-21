from django.shortcuts import render
from django.shortcuts import redirect

from hashlib import sha256

from .models import Usuario


def index(request):
    if request.session.get('usuario'):
        usuario_logado = request.session.get('usuario')
        usuario = Usuario.objects.get(id=request.session['usuario'])
        
        return render(request, 'index.html', {'usuario_logado': usuario_logado,
                                              'usuario': usuario                                   
        })
    else:
        redirect('/login/') 
    

def tabela(request):
    return render(request,
                  'tables.html'
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

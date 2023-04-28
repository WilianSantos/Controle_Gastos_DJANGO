from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import HttpResponse, JsonResponse

from hashlib import sha256
from datetime import datetime
from statistics import mean

from .models import Usuario, Rendas, Gastos

from .forms import AdicionarRenda, AdicionarGasto


def index(request):
    if request.session.get('usuario'):
        usuario_logado = request.session.get('usuario')    
        usuario = Usuario.objects.get(id=request.session['usuario'])
        
        rendas = Rendas.objects.filter(usuario=request.session['usuario'])
        renda_total = 0
        for renda in rendas:
            renda_total += renda.renda_principal
            renda_total += renda.renda_secundaria
       
        form_renda = AdicionarRenda()
        form_renda.fields['usuario'].initial = request.session['usuario']
        
        gastos = Gastos.objects.filter(usuario=request.session['usuario'])
        mes_atual = datetime.today().month
        gasto_mes = 0
        for gasto in gastos:
            if gasto.data.month == mes_atual:
                gasto_mes += gasto.valor
                
            renda_total -= gasto.valor
            
        form_gasto = AdicionarGasto()
        form_gasto.fields['usuario'].initial = request.session['usuario']            
        
        return render(request, 'index.html', {'usuario_logado': usuario_logado,
                                              'usuario': usuario,
                                              'form_renda': form_renda,
                                              'rendas': rendas,
                                              'gastos': gastos,
                                              'form_gasto': form_gasto,
                                              'gasto_mes': gasto_mes,
                                              'renda_total': renda_total                              
        })
    else:
        redirect('/') 
    
    
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

    if len(senha) < 6:
        return redirect('/registrar/?status=2')
    
    if senha != confirma_senha:
        return redirect('/registrar/?status=3')

    if len(usuario) > 0:
        return redirect('/registrar/?status=4')



    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, senha=senha, email=email)
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
        return redirect('/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/index/')

    return redirect('/')


def sair(request):
    request.session.flush()
    return redirect('/')


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
    return redirect('/?status=2')


def alterar_renda(request):
    renda_id = request.POST.get('renda_id')
    renda_principal = request.POST.get('renda_principal')
    renda_secundaria = request.POST.get('renda_secundaria')
    
    renda = Rendas.objects.get(id=renda_id)
    if renda.usuario.id == request.session['usuario']:
        
        renda.renda_principal = float(renda_principal.replace(',', '.'))
        renda.renda_secundaria = float(renda_secundaria.replace(',', '.'))
        renda.save()
        return redirect('/tabela_renda/')
    else:
        return redirect('/')
    
    
def excluir_renda(request, id):
    renda = Rendas.objects.get(id=id).delete()
    return redirect('/tabela_renda/')


def tabela_renda(request):
    rendas = Rendas.objects.filter(usuario=request.session['usuario'])
    
    return render(request, 'tables/table_renda.html', {'rendas': rendas})

def adicionar_gasto(request):
    if request.method == 'POST':
        form_gasto = AdicionarGasto(request.POST)
        
        if form_gasto.is_valid:
            form_gasto.save()
            return redirect('/index/')
        else:
            return redirect('/index/')
        
        
def ver_gasto(request, id):
    if request.session.get('usuario'):
        gasto = Gastos.objects.get(id=id)
        if request.session.get('usuario') == gasto.usuario.id:
            return render(request, 'forms/form_gasto.html', {'gasto': gasto})
        else:
            return HttpResponse('Esta não é uma renda sua') 
    else:
        return redirect('/')
    
    
def alterar_gasto(request):
    gasto_id = request.POST.get('gasto_id')
    gasto_nome = request.POST.get('gasto_nome')
    gasto_valor = request.POST.get('gasto_valor')
    
    gasto = Gastos.objects.get(id=gasto_id)
    if gasto.usuario.id == request.session['usuario']:
        
        gasto.gasto = gasto_nome
        gasto.valor = float(gasto_valor.replace(',', '.'))
        gasto.save()
        return redirect('/tabela_gasto/')
    else:
        return redirect('/')
    
    
def excluir_gasto(request, id):
    gasto = Gastos.objects.get(id=id).delete()
    return redirect('/tabela_gasto/')


def tabela_gasto(request):
    gastos = Gastos.objects.filter(usuario=request.session['usuario'])
    
    return render(request, 'tables/table_gasto.html', {'gastos': gastos})


def graficos(request):
    return render(request, 'charts/charts.html')


def relatorio_gastos(request):
    x = Gastos.objects.filter(usuario=request.session['usuario'])
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.valor for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)


def relatorio_rendas(request):
    x = Rendas.objects.filter(usuario=request.session['usuario'])
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.renda_principal for i in x if i.data.month == mes and i.data.year == ano])
        y += sum([i.renda_secundaria for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)


def relatorio_renda_gasto(request):
    rendas = Rendas.objects.filter(usuario=request.session['usuario'])
    gastos = Gastos.objects.filter(usuario=request.session['usuario'])
    
    
    meses_renda = []
    meses_gasto = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.renda_principal for i in rendas if i.data.month == mes and i.data.year == ano])
        y += sum([i.renda_secundaria for i in rendas if i.data.month == mes and i.data.year == ano])
        meses_renda.append(y)
        
        x = sum([i.valor for i in gastos if i.data.month == mes and i.data.year == ano])
        meses_gasto.append(x)
    
    data = []
    labels = ['Média Renda', 'Média Gasto']
    media_renda = mean(meses_renda)
    data.append(media_renda)
    media_gasto = mean(meses_gasto)
    data.append(media_gasto)
    
    data_json = {'data': data[::1], 'labels': labels[::1]}
     
    return JsonResponse(data_json)
    
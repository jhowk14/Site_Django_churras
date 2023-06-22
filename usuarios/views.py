from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import get_object_or_404, redirect, render
from churras.models import Prato
from django.contrib import auth, messages
from django.core.paginator import Paginator

def login(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        senha = request.POST['senha']
        if email == "" or senha == "":
            #print('Os campos email e senha não podem ficar em branco')
            messages.error(request,'Os campos email e senha não podem ficar em branco' )
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list( 'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user) 
                #print('Login realizado com sucesso')
                messages.success(request,'Login realizado com sucesso') 
                return redirect('dashboard')
            else:
                #print('A senha está incorreta!')
                messages.error(request,'A senha está incorreta!' )
                
        else:
            #print('Digite um e-mail válido')
            messages.error(request,'Digite um e-mail válido' )        
    return render(request, 'login.html')

def logout(request):
    auth.logout(request) 
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        pratos = Prato.objects.order_by('-date_prato').filter( pessoa=id)
        paginator = Paginator(pratos, 3) 
        page = request.GET.get('page') 
        pratos_por_pagina = paginator.get_page(page)
        dados = { 'lista_pratos' : pratos_por_pagina }
        return render(request, 'dashboard.html', dados)
    else:
        return redirect('index')

def cria_prato(request):
    if request.method == 'POST':
        nome_prato = request.POST['nome_prato']
        ingredientes = request.POST['ingredientes'] 
        modo_preparo = request.POST['modo_preparo'] 
        tempo_preparo = request.POST['tempo_preparo'] 
        rendimento = request.POST['rendimento'] 
        categoria = request.POST['categoria'] 
        foto_prato = request.FILES['foto_prato']
        user = get_object_or_404(User, pk=request.user.id) 
        prato = Prato.objects.create(pessoa=user, nome_prato=nome_prato, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_prato=foto_prato)
        prato.save()
        return redirect('dashboard')
    else:
        return render(request,'cria_prato.html')
    
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome'] 
        email = request.POST['email'] 
        senha = request.POST['password']
        senha2 = request.POST['password2'] 
        if not nome.strip():
            print('O campo nome não pode ficar em branco') 
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco') 
            return redirect('cadastro')
        if senha != senha2:
            #print('As senhas não são iguais')
            messages.error(request,'As senhas não são iguais' ) 
            return redirect('cadastro')
        if User.objects.filter(email=email).exists(): 
            #print('Usuário já cadastrado.')
            messages.error(request,'Usuário já cadastrado.' ) 
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        #print('Usuário cadastrado com sucesso')
        messages.success(request,'Usuário cadastrado com sucesso') 
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def edita_prato(request, prato_id): 
    prato = get_object_or_404(Prato, pk=prato_id) 
    prato_a_editar = {'prato':prato} 
    return render(request,'edita_prato.html', prato_a_editar)

def atualiza_prato(request): 
    if request.method == 'POST': 
        prato_id = request.POST['prato_id'] 
        p = Prato.objects.get(pk=prato_id) 
        p.nome_prato = request.POST['nome_prato'] 
        p.ingredientes = request.POST['ingredientes'] 
        p.modo_preparo = request.POST['modo_preparo'] 
        p.tempo_preparo = request.POST['tempo_preparo'] 
        p.rendimento = request.POST['rendimento'] 
        p.categoria = request.POST['categoria'] 
        if 'foto_prato' in request.FILES: 
            p.foto_prato = request.FILES['foto_prato'] 
            p.save() 
            return redirect('dashboard')

def deleta_prato(request, prato_id): 
    prato = get_object_or_404(Prato, pk=prato_id) 
    prato.delete() 
    return redirect('dashboard')
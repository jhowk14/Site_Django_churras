from django.shortcuts import render
from django.http import HttpResponse
from .models import Prato
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    #return HttpResponse('<h1>Churrasco</<h1><h2>Canes</<h2><p>Agora vai...</p>')
    #return render(request,'index.html') 
    #return render(request,'index.html',{'prato':'Costela na brasa'})
    pratos = Prato.objects.order_by('-date_prato').filter(publicado= True)
    paginator = Paginator(pratos, 3) 
    page = request.GET.get('page') 
    pratos_por_pagina = paginator.get_page(page)
    dados = {
        #'lista_pratos': Prato.objects.all() #Caso erro: pip install pylint-django
        'lista_pratos': pratos_por_pagina
    }
    return render(request,'index.html',dados)

def churrasco(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)
    prato_a_exibir = {
        'prato' : prato
    } 
    return render(request,'churrasco.html', prato_a_exibir)

def buscar(request): 
    pratos = Prato.objects.order_by('-date_prato').filter(publicado =True) 
    if 'buscar' in request.GET: 
        nome_a_buscar = request.GET['buscar'] 
        if nome_a_buscar: 
            pratos = pratos.filter(nome_prato__icontains=nome_a_buscar) 
    dados = {
        'lista_pratos' : pratos
    } 
    return render(request, 'buscar.html', dados)
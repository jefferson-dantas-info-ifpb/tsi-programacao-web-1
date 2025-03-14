from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from django.db.models import Q

def home(request):
    resposta = Produto.objects.all()
    return render(request, 'loja/home.html', {'resposta': resposta})

def preco(request):
    resposta = Produto.objects.all()
    return render(request, 'loja/preco.html', {'resposta': resposta})

def pesquisar(request):
    if request.method == 'POST':
        pesquisa = request.POST.get('pesquisa')
        resultado = Produto.objects.filter(nome__contains=pesquisa)
        return render(request, 'loja/pesquisa.html', {
            "pesquisa": pesquisa,
            "resultado": resultado
        })
    else:
        resultado = Produto.objects.all()
        return render(request, 'loja/pesquisa.html', {
            "resultado": resultado
        })


def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        qtd = request.POST.get('quantidade')
        
        novo_produto = Produto()
        novo_produto.nome = nome
        novo_produto.valor = preco
        novo_produto.estoque = qtd
        novo_produto.save()

    return render(request, 'loja/formcad.html', {})

def deletar(request):
    print("Chegou no Deletar")
    return HttpResponse("Estou no deletar")

def atualizar(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        id_fruta = request.POST.get('id')

        fruta = Produto.objects.get(id=id_fruta)
        fruta.valor = valor
        fruta.save()

    frutas = Produto.objects.all()
    return render(request, "loja/atualizar.html", {'frutas': frutas})

#############################################################

def exact(request):
    resultado = Produto.objects.get(nome__exact="Maconha")
    return HttpResponse(resultado)

def iexact(request):
    resultado = Produto.objects.get(nome__iexact="bACATe")
    return HttpResponse(resultado)

def contains(request):
    resultado = Produto.objects.get(nome__contains="ana")
    return HttpResponse(resultado)

def icontains(request):
    resultado = Produto.objects.get(nome__icontains="ANA")
    return HttpResponse(resultado)

def inn(request):
    resultado = Produto.objects.filter(nome__in=["Goiaba", "Banana"])
    return HttpResponse(resultado)

def gt(request):
    resultado = Produto.objects.filter(valor__gt=1)
    return HttpResponse(resultado)

def gte(request):
    resultado = Produto.objects.filter(valor__gte=1)
    return HttpResponse(resultado)

def lt(request):
    resultado = Produto.objects.filter(valor__lt=5)
    return HttpResponse(resultado)

def lte(request):
    resultado = Produto.objects.filter(valor__lte=5)
    return HttpResponse(resultado)

def startswith(request):
    resultado = Produto.objects.filter(nome__startswith="M")
    return HttpResponse(resultado)

def istartswith(request):
    resultado = Produto.objects.filter(nome__startswith="m")
    return HttpResponse(resultado)

def endswith(request):
    resultado = Produto.objects.filter(nome__endswith="a")
    return HttpResponse(resultado)

def iendswith(request):
    resultado = Produto.objects.filter(nome__iendswith="E")
    return HttpResponse(resultado)

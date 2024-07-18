from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def pesquisar(request):
    resultado = Produto.objects.get(id=1)
    return HttpResponse(resultado)

def cadastrar(request):
    print("Chegou no Cadastrar")
    return HttpResponse("Estou no cadastrar")

def deletar(request):
    print("Chegou no Deletar")
    return HttpResponse("Estou no deletar")

def atualizar(request):
    print("Atualzar")
    return HttpResponse("Estou no atualizar")

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

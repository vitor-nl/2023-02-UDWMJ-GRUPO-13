from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ver_produto(request):
  return render(request, 'ver_produto.html')

def carrinho(request):
  return render(request, 'carrinho.html')

def notificacoes(request):
  return render(request, 'notificacoes.html')

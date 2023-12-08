from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
# Create your views here.

def ver_produto(request):
  produtos = Produto.objects.all()

  return render(request, 'ver_produto.html', {'produtos' : produtos})

def carrinho(request):
  return render(request, 'carrinho.html')

def notificacoes(request):
  return render(request, 'notificacoes.html')



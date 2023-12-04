from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pedidos(request):
  return render(request, 'pedidos.html')

def login(request):
  return render(request, 'login.html')



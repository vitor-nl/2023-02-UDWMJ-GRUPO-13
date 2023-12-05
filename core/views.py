from django.shortcuts import render

# Create your views here.

def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)

def carrinho(request):
    template_name ='core/carrinho.html'
    context = {}
    return render(request, template_name, context)

def notificacoes(request):
    template_name ='core/notificacoes.html'
    context = {}
    return render(request, template_name, context)

def orders(request):
    template_name ='core/orders.html'
    context = {}
    return render(request, template_name, context)
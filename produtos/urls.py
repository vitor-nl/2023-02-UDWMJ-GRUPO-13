from django.urls import path
from . import views

urlpatterns = [
  path('', views.ver_produto, name="ver_produto"),
  path('carrinho/', views.carrinho, name="carrinho"),
  path('notificacoes/', views.notificacoes, name="notificacoes"),
]
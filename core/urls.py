from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('notificacoes/', views.notificacoes, name='notificacoes'),
    path('orders/', views.orders, name='orders'),

]
from django.urls import path
from . import views

urlpatterns =[
  path('clientes/', views.clientes, name="clientes"),
  path('login/', views.login, name="login")
]
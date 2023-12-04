from django.urls import path
from . import views

urlpatterns =[
  path('pedidos/', views.pedidos, name="pedidos"),
  path('login/', views.login, name="login")
]
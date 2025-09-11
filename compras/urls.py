from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro-tipo-produto/', views.cadastro_tipo_produto, name='cadastro_tipo_produto'),
    path('entrada-produto/', views.entrada_produto, name='entrada_produto'),
]

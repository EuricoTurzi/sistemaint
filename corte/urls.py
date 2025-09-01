from django.urls import path
from . import views

app_name = 'corte'

urlpatterns = [
    path('requisicoes-descartavel/', views.RequisicoesDescartavelListView.as_view(), name='requisicoes_descartavel_list'),
]

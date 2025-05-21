from django.urls import path
from .views import RegistrarTransportadoraView, DivisaoIscasView,RegistrarEstoqueView

urlpatterns = [
    path('registrar_transportadora/', RegistrarTransportadoraView.as_view(), name='registrar_transportadora'),
    path('divisao_iscas/', DivisaoIscasView.as_view(), name='divisao_iscas'),
    path('registrar_estoque/', RegistrarEstoqueView.as_view(), name='registrar_estoque'),
]
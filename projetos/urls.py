# projetos/urls.py

from django.urls import path
from .views import CriarRegistroView, ListarRegistrosView, DashboardView

urlpatterns = [
    path('novo/', CriarRegistroView.as_view(), name='criar_registro'),
    path('registros/', ListarRegistrosView.as_view(), name='listar_registros'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

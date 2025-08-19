from django.urls import path
from .views import (
    GridInternacional, GridInternacionalCreate, GridInternacionalUpdate,
    GridInternacionalDelete, GridInternacionalDetail, grid_internacional_quick_edit,
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    GridInternacionalFinalizados, grid_internacional_send_email, grid_internacional_json,clientes_sla_view,
    grid_internacional_sla_resumo
)
from . import views

urlpatterns = [
    # Grid Internacional URLs
    path('grid/', GridInternacional.as_view(), name='grid_internacional_list'),
    path('grid/create/', GridInternacionalCreate.as_view(), name='grid_internacional_create'),
    path('grid/<int:pk>/update/', GridInternacionalUpdate.as_view(), name='grid_internacional_update'),
    path('grid/<int:pk>/delete/', GridInternacionalDelete.as_view(), name='grid_internacional_delete'),
    path('grid/<int:pk>/detail/', GridInternacionalDetail.as_view(), name='grid_internacional_detail'),
    path('grid/quick-edit/', grid_internacional_quick_edit, name='grid_internacional_quick_edit'),
    path('grid/finalizados/', GridInternacionalFinalizados.as_view(), name='grid_internacional_finalizados'),
    path('grid/send_email/', grid_internacional_send_email, name='grid_internacional_send_email'),
    path('grid/json/', grid_internacional_json, name='grid_internacional_json'),
    path('grid/sla-resumo/', grid_internacional_sla_resumo, name='grid_internacional_sla_resumo'),
  
    # Cliente Nestle URLs
    path('clientes/', ClienteListView.as_view(), name='clientes_nestle_list'),
    path('clientes/create/', ClienteCreateView.as_view(), name='clientes_nestle_create'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='clientes_nestle_update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='clientes_nestle_delete'),
    path('clientes/controle/', clientes_sla_view, name='clientes_sla'),
    path('valores-mensais/', views.ValoresMensaisView.as_view(), name='valores_mensais'),
    path('atualizar-valor-mensal/', views.atualizar_valor_mensal, name='atualizar_valor_mensal'),
    path('clientes/json/', views.clientes_nestle_json, name='clientes_nestle_json'),
]


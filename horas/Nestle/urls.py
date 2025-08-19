from django.urls import path
from . import views
from .views import (
    GridInternacional, GridInternacionalCreate, GridInternacionalUpdate,
    GridInternacionalDelete, GridInternacionalDetail, grid_internacional_quick_edit,
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    GridInternacionalFinalizados, grid_internacional_send_email, grid_internacional_json,clientes_sla_view,
    grid_internacional_sla_resumo,CotacaoCreateView,CotacaoCreateView, CargaStatusUpdateView,
    MemoriaCalculoCreateView
)

urlpatterns = [
    # Grid Internacional URLs
    path('grid/', views.GridInternacional.as_view(), name='grid_internacional_list'),
    path('grid/finalizados/', views.GridInternacionalFinalizados.as_view(), name='grid_internacional_finalizados'),
    path('grid/novo/', views.GridInternacionalCreate.as_view(), name='grid_internacional_create'),
    path('grid/<int:pk>/editar/', views.GridInternacionalUpdate.as_view(), name='grid_internacional_update'),
    path('grid/<int:pk>/excluir/', views.GridInternacionalDelete.as_view(), name='grid_internacional_delete'),
    path('grid/<int:pk>/', views.GridInternacionalDetail.as_view(), name='grid_internacional_detail'),
    path('grid/quick-edit/', views.grid_internacional_quick_edit, name='grid_internacional_quick_edit'),
    path('grid/send-email/', views.grid_internacional_send_email, name='grid_internacional_send_email'),
    path('grid/api/', views.grid_internacional_api, name='grid_internacional_api'),
    path('grid/json/', views.grid_internacional_json, name='grid_internacional_json'),
    path('grid/sla-resumo/', grid_internacional_sla_resumo, name='grid_internacional_sla_resumo'),
  
    # Cliente Nestle URLs
    path('clientes/', views.ClienteListView.as_view(), name='clientes_nestle_list'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='clientes_nestle_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='clientes_nestle_update'),
    path('clientes/<int:pk>/excluir/', views.ClienteDeleteView.as_view(), name='clientes_nestle_delete'),
    path('clientes/sla/', views.clientes_sla_view, name='clientes_sla'),
    path('clientes/json/', views.clientes_nestle_json, name='clientes_nestle_json'),
    path('valores-mensais/', views.ValoresMensaisView.as_view(), name='valores_mensais'),
    path('valores-mensais/atualizar/', views.atualizar_valor_mensal, name='atualizar_valor_mensal'),
    path('controle/lista', views.CotacaoListView.as_view(), name='cotacoes-listar'),
    path('controle/nova/', views.CotacaoCreateView.as_view(), name='cotacoes-criar'),
    path('controle/aprovar/<int:pk>/<str:status>/', views.CargaStatusUpdateView.as_view(), name='carga-aprovar-reprovar'),
    # URLs para MemoriaCalculo
    path('memoria-calculo/novo/', views.MemoriaCalculoCreateView.as_view(), name='memoria-calculo-criar'),
]
    



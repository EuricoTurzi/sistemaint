from django.urls import path
from .views import FaturamentoListView, update_status_faturamento, contratosListView, formularioCreateView,FinanceirohListViews,atualizar_observacoes,external_vouchers_list

urlpatterns = [
    path('', FaturamentoListView.as_view(), name='faturamento_list'),
    path('contrato', contratosListView.as_view(), name='Contrato_list'),
    path('FinanceirohListViews', FinanceirohListViews.as_view(), name='FinanceirohListViews'),
    path('atualizar_status_faturamento/<int:id>/', update_status_faturamento, name='atualizar_status_faturamento'),
    
    path('formulario/create/', formularioCreateView.as_view(), name='formulario_create'),
        path('atualizar_observacoes/<int:id>/', atualizar_observacoes, name='atualizar_observacoes'),
       path('externos/', external_vouchers_list, name='external_vouchers_list'),
    
]

from django.urls import path
from .views import RequisicoesListView, ReativacaoView, ReativacaoIdIccidCreateView, ReativacaoListView,update_status
from django.urls import path
from .views import DownloadPdfView

urlpatterns = [
    path('reativacoes/', ReativacaoListView.as_view(), name='reativacao_list'),
    path('reativacoes/adicionar/', ReativacaoIdIccidCreateView.as_view(), name='reativacao_id_iccid_adicionar'),
    path('reativacao/', ReativacaoView.as_view(), name='reativacao'),
    path('update_status/', update_status, name='update_status'),
    path('requisicoes/', RequisicoesListView.as_view(), name='requisicoes_list'),
    path('download_pdf/<int:id_iccid>/', DownloadPdfView.as_view(), name='download_pdf_REATIVACAO'),
]


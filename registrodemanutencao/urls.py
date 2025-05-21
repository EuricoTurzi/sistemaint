from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    FormularioListView,
    FormulariosCreateView,
    FormularioDetailView,
    FormulariosUpdateView,
    aprovar_manutencao,
    reprovar_manutencao,
    CreateView,
    
    ConfiguracaoListView,
    expedicaoListView,
    expedicaoDetailView,
    configDetailView,
    historico_manutencaoListView,
    entradasListView,
    download_pdf,
    CriarRetornoView,
    DownloadPDFView,
    ListaRetornosView,
    reprovar_manutencao2,
    download_protocolo_entrada,
    editado_manutencao
)
urlpatterns = [
    path('configlist/historico', historico_manutencaoListView.as_view(), name='historico_manutencaoListView'),
    path('configlist/entradaslist', entradasListView.as_view(), name='entradasListView'),
    path('registrodemanutencao/create/', FormulariosCreateView.as_view(), name='FormulariosCreateView'),
    path('registrodemanutencao/<int:pk>/update/', FormulariosUpdateView.as_view(), name='FormulariosUpdateView'),
    path('registrodemanutencao/<int:pk>/detail/', FormularioDetailView.as_view(), name='FormularioDetailView'),
    path('aprovado/<int:id>/', aprovar_manutencao, name='Aprovado_Inteligência'),
    path('reprovado/<int:id>/', reprovar_manutencao, name='Reprovado_Inteligência'),
    path('reprovado2/<int:id>/', reprovar_manutencao2, name='Reprovado_Inteligência2'),
    path('protocolo/<int:pk>/', download_protocolo_entrada, name='download_protocolo_entrada'),
    path('editado/<int:pk>/', editado_manutencao, name='editado_manutencao'),
    path('manutencaonova/<int:id>/', CreateView.as_view(), name='manutencaonova'),
    path('download-pdf/<int:pk>/', download_pdf, name='download_pdfmanutencao'),
    path('lista_retornos/', ListaRetornosView.as_view(), name='lista_retornos'),
     path('criar_retorno/', CriarRetornoView.as_view(), name='criar_retorno'),
    path('download_pdf/<int:pk>/', DownloadPDFView.as_view(), name='download_pdf'),
    path('expedicao/', expedicaoListView.as_view(), name='expedicao_list'),
    path('expedicao/<int:pk>/', expedicaoDetailView.as_view(), name='expedicao_detail'),
    path('configdetail/<int:pk>/', configDetailView.as_view(), name='config_detail'),
    path('registrodemanutencao/<int:pk>/update/', FormulariosUpdateView.as_view(), name='registrodemanutencao_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

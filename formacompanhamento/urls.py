from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    formulariorateview,
    AcompanhamentoListView,
    AgentesListView,
    agenteCreateView,
    agenteUpdateView,
    get_agente_data,
    RegistroPagamentoListView,
    RegistroPagamentoCreateView,
    RegistroPagamentoUpdateView,
    RegistroPagamentoDeleteView,
    nova_tabela_view,
    atualizar_registro,
    download_pdf,
    validar,
    FormularioView,
    PrestadorCreateView,
    PrestadorListView,
    get_prestador_data,
    ClientesAcionamentoCreateView,
    ClientesAcionamentoListView,
    RegistroPagamentoUpdateView,
    obter_dados_registro,
    obter_dados_cliente,
    TotalFormView,
    TabelaRegistrosView,
    ClienteUpdateView,
    prestadoresupdate,
    
)

# Definindo o namespace do app
app_name = 'formacompanhamento'

urlpatterns = [
    # Formas de Acompanhamento
    path('formacompanhamento/create/', formulariorateview.as_view(), name='formacompanhamento'),
    path('formacompanhamento/lista/', AcompanhamentoListView.as_view(), name='facomp'),

    # Formulário Geral
    path('formulario/<int:pk>/', FormularioView.as_view(), name='formulario'),

    # Agentes
    path('agentes/lista/', AgentesListView.as_view(), name='agentesListView'),
    path('agentes/novo/', agenteCreateView.as_view(), name='agenteCreateView'),
    path('agentes/<int:pk>/editar/', agenteUpdateView.as_view(), name='agenteUpdateView'),
    path('agentes/dados/<int:agente_id>/', get_agente_data, name='get_agente_data'),
    path('totalform/', TotalFormView.as_view(), name='totalform_view'),

    # Prestadores
      path('prestador/novo/', PrestadorCreateView.as_view(), name='criar_prestador'),
    path('prestadores/lista/', PrestadorListView.as_view(), name='lista_prestadores'),
    path('get-prestador-data/', get_prestador_data, name='get_prestador_data'),
    path('tabela/', TabelaRegistrosView.as_view(), name='tabela_registros'),

    # Registro de Pagamento
    path('registro_pagamento/', RegistroPagamentoListView.as_view(), name='registro_pagamento_list'),
    path('registro_pagamento/novo/', RegistroPagamentoCreateView.as_view(), name='registro_pagamento_create'),
    path('registro_pagamento/<int:pk>/editar/', RegistroPagamentoUpdateView.as_view(), name='registro_pagamento_update'),
    path('registro_pagamento/<int:pk>/excluir/', RegistroPagamentoDeleteView.as_view(), name='registro_pagamento_delete'),
    path('registro_pagamento/<int:pk>/validar/', validar, name='validar'),

    # API e PDF
    path('registro_pagamento/<int:pk>/download/', download_pdf, name='download_pdf'),
    path('atualizar-registro/', atualizar_registro, name='atualizar_registro'),
    path('clientes-acionamento/criar/', ClientesAcionamentoCreateView.as_view(), name='create_clientes_acionamento'),
    path('clientes-acionamento/lista/', ClientesAcionamentoListView.as_view(), name='clientes_acionamento_list'),
    path('clientes-acionamento/<int:pk>/update/', RegistroPagamentoUpdateView.as_view(), name='clientes_acionamento_update'),
    path('clientes-acionamento2/<int:pk>/update/', ClienteUpdateView.as_view(), name='ClienteUpdateView'),
    # Nova Tabela
    path('nova-tabela/', nova_tabela_view, name='nova_tabela'),
    path('download-pdf/<int:instance_id>/',download_pdf, name='download_pdf'),
    
    path('registro/<int:registro_id>/dados/', views.obter_dados_registro, name='registro_dados'),
    path('cliente/<int:cliente_id>/dados/', views.obter_dados_cliente, name='cliente_dados'),
    path("prestadores/editar/<int:pk>/", prestadoresupdate.as_view(), name="editar_prestador"),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from .views import (
    paradaCreateView, 
    paradaListView, 
    get_choices, 
    passagemCreateView,
    PassagemListView, 
    get_pa_choices, 
    ParadaDetailView,
    RegistrarSaidaView,
    historicoListView,
    Parada2DetailView,
)

urlpatterns = [
    path('pparada/', paradaCreateView.as_view(), name='paradaseguraform'),
    path('pa_list/', paradaListView.as_view(), name='paradaseguralist'),
    path('get-choices/', get_choices, name='get_choices'),
    path('passagem/', passagemCreateView.as_view(), name='passagemCreateView'),
    path('historico/', PassagemListView.as_view(), name='historico_passagem'),
    path('historico_parada/', historicoListView.as_view(), name='historico_parada'),
    path('get_pa_choices/', get_pa_choices, name='get_pa_choices'),
    path('parada/<int:pk>/detail/', ParadaDetailView.as_view(), name='ParadaDetailView'),
    path('parada2/<int:pk>/detail/', Parada2DetailView.as_view(), name='Parada2DetailView'),
    path('parada/<int:pk>/registrar-saida/', RegistrarSaidaView.as_view(), name='registrar_saida'),
]

# Inclua esta parte apenas se estiver em ambiente de desenvolvimento com DEBUG=True
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('clientes/list/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/create/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/detail/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<int:pk>/update/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    path('cliente/', views.acompanhamento_cliente, name='acompanhamento_cliente'),
    path('acompanhamento/relatorio/', views.acompanhamento_relatorio, name='acompanhamento_relatorio'),
    path('acompanhamento/requisicao/', views.acompanhamento_requisicao, name='acompanhamento_requisicao'),
    path('acompanhamento/desempenho/', views.acompanhamento_desempenho, name='acompanhamento_desempenho'),
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('cliente/list',views.clienteviews.as_view() , name='cliente_list'),  
    path('cliente/create/',views.clientecrateview.as_view(),name='cliente_create'),
    path('cliente/<int:pk>/detail/',views.clientedetailview.as_view(), name='cliente_detail'),
    path('cliente/<int:pk>/update/',views.clienteupdateview.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.clientedeleteview.as_view(), name='cliente_delete'),
    path('cliente/', views.acompanhamento_cliente, name='acompanhamento_cliente'),
    path('mensal/', views.acompanhamento_relatorio, name='acompanhamento_relatorio'),
    path('anual/', views.acompanhamento_requisicao, name='acompanhamento_requisicao'),
    path('desempenho/', views.acompanhamento_desempenho, name='acompanhamento_desempenho'),
    
]


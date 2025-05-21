from django.urls import path
from . import views

urlpatterns = [
    path('produto/list',views.produtoviews.as_view() , name='produto_list'),  
    path('produto/create/',views.produtocrateview.as_view(),name='produto_create'),
    path('produto/<int:pk>/detail/',views.produtodetailview.as_view(), name='produto_detail'),
    path('produto/<int:pk>/update/',views.produtoupdateview.as_view(), name='produto_update'),
    path('produto/<int:pk>/delete/', views.produtodeleteview.as_view(), name='produto_delete'),
    path('acompanhamento_cliente/', views.acompanhamento_cliente, name='acompanhamento_cliente'),
    path('acompanhamento/relatorio/', views.acompanhamento_relatorio, name='acompanhamento_relatorio'),
    path('acompanhamento/anual/', views.acompanhamento_requisicao, name='acompanhamento_anual'),
    path('acompanhamento/desempenho/', views.acompanhamento_desempenho, name='acompanhamento_desempenho'),
   
]
from django.urls import path
from . import views

urlpatterns = [
    path('estoque/list', views.EstoqueViews.as_view(), name='estoque_list'),  
    path('estoque/create/', views.EstoqueCreateView.as_view(), name='estoque_create'),
    path('estoque/<int:pk>/detail/', views.EstoqueDetailView.as_view(), name='estoque_detail'),
     path('estoque/update/<int:id>/', views.estoque_update, name='estoque_update'),
]
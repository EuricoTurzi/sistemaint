from django.urls import path
from . import views

urlpatterns = [
    path('saidas/list', views.SaidasViews.as_view(), name='saidas_list'),  
    path('saidas/create/', views.SaidasCreateView.as_view(), name='saidas_create'),
    path('saidas/<int:pk>/detail/', views.SaidasDetailView.as_view(), name='saidas_detail'),
]
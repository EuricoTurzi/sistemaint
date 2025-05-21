from django.urls import path
from .views import LembretesView, DeletarLembreteView

urlpatterns = [
    path('', LembretesView.as_view(), name='lembretes'),
    path('deletar/<int:pk>/', DeletarLembreteView.as_view(), name='deletar_lembrete'),
]

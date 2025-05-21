from django.urls import path
from .views import T42ModelListView, T42ModelCreateView, UpdateEstoqueStatusView, RegistrarEstoqueT42View

urlpatterns = [
    path('t42/', T42ModelListView.as_view(), name='t42_view'),
    path('t42/create/', T42ModelCreateView.as_view(), name='t42_create'),
    path('t42/update/<int:pk>/', UpdateEstoqueStatusView.as_view(), name='update_estoque_status'),
    path('registrar_estoque_t42/', RegistrarEstoqueT42View.as_view(), name='registrar_estoque_t42'),
]
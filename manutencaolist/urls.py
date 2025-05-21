from django.urls import path
from . import views
from .views import FormularioDeleteView

urlpatterns = [
    path('manutencaolist',views.FormularioListView.as_view(), name='manutencaolist'),  
    path('manutencaocreate',views.FormulariosCreateView.as_view(),name='registrodemanutencao'),
    path('manutencaodetail/<int:pk>/detail/', views.FormularioDetailView.as_view(), name='manutencaodetail_detail'),
    path('manutencaoup/<int:pk>/update/',views.FormulariosUpdateView.as_view(), name='manutencao_update'),
    

]
from django.urls import path
from .views import cadastroCreateView,CadastroUpdateView,perfilUpdateView,perfilCreateView,cadastroListView,perfilListView

urlpatterns = [
path('cadastro/', cadastroCreateView.as_view(),name='cadastro_create'),    
path('pesquisa/',perfilCreateView.as_view(),name='pesquisa_create'),
path('cadastro_list/',cadastroListView.as_view(),name='cadastro_list'),
path('pesquisa_list',perfilListView.as_view(),name='pesquisa_list'),
path('cadastro/<int:pk>/update/',perfilUpdateView.as_view(),name='cadastro_update'),
path('pesquisa/<int:pk>/update/',CadastroUpdateView.as_view(),name= 'pesquisa_update')    
]

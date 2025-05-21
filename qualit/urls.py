from django.urls import path
from . import views

urlpatterns = [
   
    path('criar-qualit/', views.QualitCreateView.as_view(), name='criar_qualit'),
    path('', views.QualitListView.as_view(), name='listar_qualits'),

]
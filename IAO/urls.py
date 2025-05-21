from django.urls import path
from . import views

urlpatterns = [
    path('iao_list/', views.IAOListView.as_view(), name='iao_list'),
    path('iao_create/', views.IAOCreateView.as_view(), name='iao_create'),
]
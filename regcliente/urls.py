from django.urls import path
from .views import RegclienteCreateView, RegclienteListViews

urlpatterns = [
     path('', RegclienteCreateView.as_view(), name='regcliente'),
    path('regcliente/list/', RegclienteListViews.as_view(), name='regcliente_list')

]
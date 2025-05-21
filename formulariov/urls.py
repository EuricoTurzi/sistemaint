from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulariov, name='formulariosv'),

]
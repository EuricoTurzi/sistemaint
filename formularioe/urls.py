from django.urls import path
from . import views
from .views import formularioeCreateView
urlpatterns = [
    
    path('', views.formularioeCreateView.as_view(), name='formularioe_create'),
]
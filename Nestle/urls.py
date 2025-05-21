from django.urls import path
from .views import GridInternacionalCreateView,GridInternacional

urlpatterns = [
    path('nestle_form', GridInternacionalCreateView.as_view(), name='nestle_form'),
    path('nestle_list',GridInternacional.as_view(),name="nestle_list"),
    
]

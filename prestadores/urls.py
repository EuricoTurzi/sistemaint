from django.urls import path
from .views import RprestadorCreateView, RprestadorListViews

urlpatterns = [
     path('', RprestadorCreateView.as_view(), name='rprestador'),
    path('rprestador/list/', RprestadorListViews.as_view(), name='prestador_list')
]

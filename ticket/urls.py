from django.urls import path
from .views import ticketCreateView, ticketListView,atualizar_status,atualizar_status2
from . import views
urlpatterns = [
    path('ticket/', ticketCreateView.as_view(), name='ticketCreateView'),
    path('ticket_list/', ticketListView.as_view(), name='ticketListView'),
    path('atualizar_status/<int:ticket_id>/', views.atualizar_status, name='atualizar_status'),
    path('atualizar_status2/<int:ticket_id>/', views.atualizar_status2, name='atualizar_status2'),
]
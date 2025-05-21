from .views import cadastrar_horas,consulta_horas,HorasUpdateView,aprovar_horas,consulta_horas_pdf,enviar_email_relatorio_horas
from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar-horas', views.cadastrar_horas, name='cadastrar_horas'),
    path('consulta-horas', views.consulta_horas, name='consultar_horas'),
    path('horas/update/<int:pk>/', HorasUpdateView.as_view(), name='update_horas'),
    path('aprovar/<int:pk>/', views.aprovar_horas, name='aprovar_horas'),
    path('consulta-horas/pdf/', views.consulta_horas_pdf, name='consulta_horas_pdf'),
     path(
        'consulta-horas/enviar-email/',
        enviar_email_relatorio_horas,
        name='enviar_email_relatorio_horas'
    ),
     path('horas/validar/', views.validar_hora, name='validar_hora'),
    
   
]

from django.urls import path
from .views import PdfListView
urlpatterns = [
    path('pdfs/',PdfListView.as_view(), name=  'pdf_list'),
]

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import GridInternacional
from .forms import GridInternacionalForm
# Create your views here.

class GridInternacionalCreateView(CreateView):
    model = GridInternacional
    form_class =  GridInternacionalForm
    template_name = "grid_internacional_form.html"
    success_url = reverse_lazy('grid-list') 
    
class GridInternacional(ListView):
    model = GridInternacional
    template_name = 'grid_internacional_list.html'
    context_object_name = 'grids'
from django.shortcuts import render

# Create your views here.

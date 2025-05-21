
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import IAOmodels
from .forms import IAOForm

class IAOListView(ListView):
    model = IAOmodels
    template_name = 'iao_list.html'
    context_object_name = 'iao'

class IAOCreateView(CreateView):
    model = IAOmodels
    form_class = IAOForm
    template_name = 'iao_create.html'
    success_url = reverse_lazy('iao_list')


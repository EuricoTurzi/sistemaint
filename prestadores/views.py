from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Prestador
from .forms import Prestadorform
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class RprestadorCreateView( PermissionRequiredMixin,LoginRequiredMixin,  CreateView):
    model = Prestador
    template_name = 'rprestador.html'
    form_class = Prestadorform
    success_url = reverse_lazy('rprestador')
    permission_required = 'prestadores.add_rprestador'  # Substitua 'prestadores' pelo nome do seu aplicativo

class RprestadorListViews( PermissionRequiredMixin,LoginRequiredMixin,  ListView):
    model = Prestador
    template_name = "prestador.html"
    context_object_name = 'prestador_list'
 
    permission_required = 'prestadores.view_rprestador'  # Substitua 'prestadores' pelo nome do seu aplicativo

class RequisicoesUpdateView( PermissionRequiredMixin,LoginRequiredMixin,  UpdateView):
    model = Prestador
    template_name = 'rprestador.html'
    form_class = Prestadorform
    success_url = reverse_lazy('Rprestador')
    permission_required = 'prestadores.change_rprestador'  # Substitua 'prestadores' pelo nome do seu aplicativo

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import regcliente
from .forms import regclientes
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class RegclienteCreateView( PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = regcliente
    template_name = 'regclientes.html'
    form_class = regclientes
    success_url = reverse_lazy('regcliente_list')
    permission_required = 'regcliente.add_regcliente'  # Substitua 'regcliente' pelo nome do seu aplicativo

class RegclienteUpdateView( PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = regcliente
    template_name = 'regclientes.html'
    form_class = regclientes
    success_url = reverse_lazy('regcliente_list')
    permission_required = 'regcliente.change_regcliente'  # Substitua 'regcliente' pelo nome do seu aplicativo

class RegclienteListViews( PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = regcliente
    template_name = "regclientes_list.html"
    context_object_name = 'regclientes_list'
   
    permission_required = 'regcliente.view_regcliente'  # Substitua 'regcliente' pelo nome do seu aplicativo

from typing import Any
from . import models
from . import forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import formularioe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class formularioeListView( PermissionRequiredMixin,LoginRequiredMixin,  ListView):
    model = models.formularioe
    template_name = "formularioe.html"
    context_object_name = 'formularioe'
    paginate_by = 5
    permission_required = 'formularioe.view_formularioe'  # Substitua 'formularioe' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

from .forms import formularioeForm
from .models import formularioe

class formularioeCreateView( PermissionRequiredMixin,LoginRequiredMixin,  CreateView):
    model = formularioe
    template_name = 'formularioe_create.html'
    form_class = formularioeForm
    success_url = reverse_lazy('formularioe_create')
    permission_required = 'formularioe.add_formularioe'  # Substitua 'formularioe' pelo nome do seu aplicativo

class formularioeDetailView( PermissionRequiredMixin,LoginRequiredMixin,  DetailView):
    model = models.formularioe
    template_name = 'formularioe_detail.html'
    permission_required = 'formularioe.view_formularioe'  # Substitua 'formularioe' pelo nome do seu aplicativo

class ClienteUpdateView( PermissionRequiredMixin,LoginRequiredMixin,  UpdateView):
    model = models.Clientes
    template_name = 'cliente_update.html'
    form_class = forms.formularioeForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'formularioe.change_clientes'  # Substitua 'formularioe' pelo nome do seu aplicativo

class formularioeDeleteView( PermissionRequiredMixin,LoginRequiredMixin,  DeleteView):
    model = models.formularioe
    template_name = 'formularioe_delete.html'
    success_url = reverse_lazy('formularioe_list')
    permission_required = 'formularioe.delete_formularioe'  # Substitua 'formularioe' pelo nome do seu aplicativo

@login_required
def formularioe(request):
    return render(request, 'formularioe_create.html')

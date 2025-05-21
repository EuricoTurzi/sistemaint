from typing import Any
from .forms import ClienteForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class clienteviews(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Cliente
    template_name = "cliente_list.html"
    context_object_name = 'cliente'
    paginate_by = 15
    permission_required = 'cliente.view_cliente'  # Substitua 'cliente' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

class clientecrateview(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Cliente
    template_name = 'cliente_create.html'
    form_class = forms.ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'cliente.add_Cliente'  # Substitua 'cliente' pelo nome do seu aplicativo

class clientedetailview(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Cliente
    template_name = 'cliente_detail.html'
    permission_required = 'cliente.view_Cliente'  # Substitua 'cliente' pelo nome do seu aplicativo

class clienteupdateview(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Cliente
    template_name = 'cliente_update.html'
    form_class = forms.ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'cliente.change_Cliente'  # Substitua 'cliente' pelo nome do seu aplicativo

class clientedeleteview(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Cliente
    template_name = 'cliente_delete.html'
    success_url = reverse_lazy('cliente_list')
    permission_required = 'cliente.delete_Cliente'  # Substitua 'cliente' pelo nome do seu aplicativo

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def acompanhamento_cliente(request):
    return render(request, 'acompanhamento_cliente.html')

@login_required
def acompanhamento_relatorio(request):
    return render(request, 'acompanhamento_relatorio.html')

@login_required
def acompanhamento_requisicao(request):
    return render(request, 'acompanhamento_requisicao.html')

@login_required
def acompanhamento_desempenho(request):
    return render(request, 'acompanhamento_desempenho.html')

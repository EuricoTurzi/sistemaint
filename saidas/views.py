from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class SaidasViews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = models.Saidas
    template_name = "saidas_list.html"
    context_object_name = 'saidas_list'
    paginate_by = 5
    permission_required = "saidas.view_saidas"

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        return queryset
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Produto, Saidas
from .forms import SaidasForm

class SaidasCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Saidas
    template_name = 'saidas_create.html'
    form_class = SaidasForm
    success_url = reverse_lazy('saidas_list')
    permission_required = "saidas.add_saidas"

    def form_valid(self, form):
        saida = form.save(commit=False)
        produto = saida.produto
        produto.quantidade -= saida.quantidade
        produto.save()
        saida.save()
        return super().form_valid(form)

class SaidasDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = models.Saidas
    template_name = 'saidas_detail.html'
    permission_required = "saidas.view_saidas"

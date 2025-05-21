from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class produtoviews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = models.Produto
    template_name = "produto_list.html"
    context_object_name = 'produto'
    paginate_by = 20
    permission_required = "produto.view_produto"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

class produtocrateview(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = models.Produto
    template_name = 'produto_create.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')
    permission_required = "produto.add_produto"

class produtodetailview(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = models.Produto
    template_name = 'produto_detail.html'
    permission_required = "produto.view_produto"

class produtoupdateview(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = models.Produto
    template_name = 'produto_update.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')
    permission_required = "produto.change_produto"

class produtodeleteview(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = models.Produto
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('produto_list')
    permission_required = "produto.delete_produto"

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

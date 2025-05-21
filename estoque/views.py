from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Estoque, Produto

from django.db.models import Sum

class EstoqueViews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Estoque
    template_name = "estoque_list.html"
    context_object_name = 'estoque_list'
    paginate_by = 5
    permission_required = "estoque.view_estoque"

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(produto__nome__icontains=nome)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = Produto.objects.all()
        total_quantidade = produtos.aggregate(total=Sum('quantidade'))['total']
        
        # Calcular a quantidade total de cada produto
        produtos_quantidade = Estoque.objects.values('produto__nome').annotate(total_quantidade=Sum('quantidade'))
        
        context['produtos'] = produtos
        context['total_quantidade'] = total_quantidade
        context['produtos_quantidade'] = produtos_quantidade
        return context





from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Produto, Estoque
from .forms import EstoqueForm

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Produto, Estoque
from .forms import EstoqueForm

class EstoqueCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Estoque
    template_name = 'estoque_create.html'
    form_class = EstoqueForm
    success_url = reverse_lazy('estoque_list')
    permission_required = "estoque.add_estoque"

    def form_valid(self, form):
        entrada = form.save(commit=False)
        produto = entrada.produto
        produto.quantidade += entrada.quantidade
        produto.save()
        entrada.save()
        return super().form_valid(form)

class EstoqueDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = models.Estoque
    template_name = 'estoque_detail.html'
    permission_required = "estoque.view_estoque"


from django.shortcuts import render, get_object_or_404, redirect
from .models import Estoque
from .forms import EstoqueForm

def estoque_update(request, id):
    estoque = get_object_or_404(Estoque, id=id)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            form.save()
            return redirect('estoque_list')
    else:
        form = EstoqueForm(instance=estoque)
    return render(request, 'estoque/estoque_form.html', {'form': form})
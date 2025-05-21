from django.views.generic import ListView, CreateView
from requisicao.models import Requisicoes, Produto, Clientes
from django.shortcuts import get_object_or_404, redirect
from . import models, forms
from .models import Formulario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from itertools import chain
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse

class FaturamentoListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "faturamento_list.html"
    context_object_name = 'requisicoes'
    paginate_by = 10
    permission_required = 'faturamento.view_formulario'  # Substitua 'faturamento' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')  # Ordena por ID em ordem decrescente
        queryset = queryset.exclude(status='Reprovado pelo CEO')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        status_faturamento = self.request.GET.get('status_faturamento_filtro')
        cliente = self.request.GET.get('cliente_filtro')
        motivo = self.request.GET.get('motivo_filtro')
        tipo_produto = self.request.GET.get('tipo_produto_filtro')
        contrato_tipo = self.request.GET.get('contrato_tipo_filtro')
        fatura_tipo = self.request.GET.get('fatura_tipo_filtro')
        status = self.request.GET.get('status')

        # Aplicar filtros
        if data_inicio and data_fim:
            queryset = queryset.filter(data__range=[data_inicio, data_fim])
        if status_faturamento:
            queryset = queryset.filter(status_faturamento=status_faturamento)
        if cliente:
            queryset = queryset.filter(nome=cliente)
        if motivo:
            queryset = queryset.filter(motivo=motivo)
        if tipo_produto:
            queryset = queryset.filter(tipo_produto=tipo_produto)
        if contrato_tipo:
            queryset = queryset.filter(contrato=contrato_tipo)
        if fatura_tipo:
            queryset = queryset.filter(tipo_fatura=fatura_tipo)
        

        # Desativar paginação se algum filtro for aplicado
        if data_inicio or data_fim or status_faturamento or cliente or motivo or tipo_produto or contrato_tipo or fatura_tipo:
            self.paginate_by = None

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_faturamento_choices'] = Requisicoes._meta.get_field('status_faturamento').choices
        context['clientes_choices'] = Clientes.objects.all()
        context['motivo_choices'] = Requisicoes._meta.get_field('motivo').choices
        context['tipo_produto_choices'] = Produto.objects.all()
        context['contrato_tipo_choices'] = Requisicoes._meta.get_field('contrato').choices
        context['fatura_tipo_choices'] = Requisicoes._meta.get_field('tipo_fatura').choices
        context['status'] = Requisicoes._meta.get_field('status').choices
        return context

def update_status_faturamento(request, id):
    if request.method == 'POST':
        requisicao = get_object_or_404(Requisicoes, id=id)
        status_faturamento = request.POST.get('status_faturamento')
        requisicao.status_faturamento = status_faturamento
        requisicao.save()
        return JsonResponse({'status': 'success', 'message': 'Status atualizado com sucesso'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


class contratosListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "contrato_list.html"
    context_object_name = 'contratos_list'
    paginate_by = 10
    permission_required = 'faturamento.view_formulario'  # Substitua 'faturamento' pelo nome do seu aplicativo

class formularioCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Formulario
    template_name = 'Formulario_contratos.html'
    form_class = forms.FormularioForm
    success_url = reverse_lazy('formulario_create')
    permission_required = 'faturamento.add_formulario'  # Substitua 'faturamento' pelo nome do seu aplicativo

from formacompanhamento.models import Formacompanhamento
class FinanceirohListViews(ListView):
    model = Formacompanhamento  # Defina o modelo aqui
    template_name = "historicodeacionamento.html"  # Substitua pelo nome do seu template
    context_object_name = 'financeiro_list'
    paginate_by = 10


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse



def atualizar_observacoes(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    if request.method == 'POST':
        observacoes = request.POST.get('observacoes')
        registro.observacoes = observacoes
        registro.save()
        return redirect('faturamento_list')  # Redireciona para
    

from django.shortcuts import render

import requests
from django.shortcuts import render
import requests
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
# faturamento/views.py

import requests
from django.shortcuts import render
from django.utils.dateparse import parse_datetime

def external_vouchers_list(request):
    url = 'https://gsvouchers.com.br/api/vouchers/'
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        vouchers = resp.json()
        for v in vouchers:
            # Converte a data de criação
            if iso := v.get('data'):
                v['data'] = parse_datetime(iso)
            # Converte a data de alteração
            if iso2 := v.get('updated_at'):
                v['updated_at'] = parse_datetime(iso2)
            # Calcula o saldo = gasto - 40
            try:
                gasto = float(v.get('valor') or 0)
                v['saldo'] = gasto - 40.0
            except (TypeError, ValueError):
                v['saldo'] = None
    except requests.RequestException:
        vouchers = []

    return render(request, 'external_vouchers_list.html', {
        'vouchers': vouchers
    })

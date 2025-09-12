from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import CadastroTipoProduto, EntradaProduto
from .forms import CadastroTipoProdutoForm, EntradaProdutoForm, FiltroEntradaProdutoForm

# Create your views here.

def index(request):
    """View principal do app compras"""
    # Buscar estatísticas para o dashboard
    total_produtos = CadastroTipoProduto.objects.count()
    total_entradas = EntradaProduto.objects.count()
    produtos_recentes = CadastroTipoProduto.objects.all()[:5]  # Últimos 5 produtos
    entradas_recentes = EntradaProduto.objects.select_related('codigo_produto').all()[:5]  # Últimas 5 entradas
    
    return render(request, 'compras/index.html', {
        'total_produtos': total_produtos,
        'total_entradas': total_entradas,
        'produtos_recentes': produtos_recentes,
        'entradas_recentes': entradas_recentes,
    })

def cadastro_tipo_produto(request):
    """View para cadastro de tipo de produto"""
    if request.method == 'POST':
        form = CadastroTipoProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('compras:cadastro_tipo_produto')
    else:
        form = CadastroTipoProdutoForm()
    
    produtos = CadastroTipoProduto.objects.all()
    return render(request, 'compras/cadastro_tipo_produto.html', {
        'form': form,
        'produtos': produtos
    })

def entrada_produto(request):
    """View para entrada de produto"""
    if request.method == 'POST':
        form = EntradaProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrada de produto registrada com sucesso!')
            return redirect('compras:entrada_produto')
    else:
        form = EntradaProdutoForm()
    
    # Filtro de equipamentos
    filtro_form = FiltroEntradaProdutoForm(request.GET)
    entradas = EntradaProduto.objects.select_related('codigo_produto').all()
    
    # Aplicar filtro se fornecido
    if filtro_form.is_valid() and filtro_form.cleaned_data.get('id_equipamento'):
        id_equipamento = filtro_form.cleaned_data['id_equipamento']
        entradas = entradas.filter(id_equipamento__icontains=id_equipamento)
    
    return render(request, 'compras/entrada_produto.html', {
        'form': form,
        'filtro_form': filtro_form,
        'entradas': entradas
    })

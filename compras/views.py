from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import CadastroTipoProduto, EntradaProduto
from .forms import CadastroTipoProdutoForm, EntradaProdutoForm

# Create your views here.

def index(request):
    """View principal do app compras"""
    return render(request, 'compras/index.html')

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
    
    entradas = EntradaProduto.objects.all()
    return render(request, 'compras/entrada_produto.html', {
        'form': form,
        'entradas': entradas
    })

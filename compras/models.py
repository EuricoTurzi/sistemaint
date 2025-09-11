from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CadastroTipoProduto(models.Model):
    """Modelo para cadastro de tipo de produto"""
    nome_produto = models.CharField(max_length=200, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição")
    fabricante = models.CharField(max_length=200, verbose_name="Fabricante")
    telefone_fabricante = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    email_fabricante = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Valor Unitário")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    class Meta:
        verbose_name = "Cadastro de Tipo de Produto"
        verbose_name_plural = "Cadastros de Tipos de Produtos"
        ordering = ['-data_cadastro']
    
    def __str__(self):
        return f"{self.nome_produto} - {self.fabricante}"

class EntradaProduto(models.Model):
    """Modelo para entrada de produto"""
    codigo_produto = models.ForeignKey(CadastroTipoProduto, on_delete=models.CASCADE, verbose_name="Código do Produto (FK)")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade")
    id_equipamento = models.CharField(max_length=100, verbose_name="ID (Número do Equipamento)")
    data = models.DateTimeField(verbose_name="Data (datetime)")
    valor_nota = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Nota (Valor de Compra)")
    numero_nota_fiscal = models.CharField(max_length=50, verbose_name="Número de Nota Fiscal")
    data_entrada = models.DateTimeField(auto_now_add=True, verbose_name="Data de Entrada")
    
    class Meta:
        verbose_name = "Entrada de Produto"
        verbose_name_plural = "Entradas de Produtos"
        ordering = ['-data_entrada']
    
    def __str__(self):
        return f"{self.codigo_produto.nome_produto} - Qtd: {self.quantidade} - NF: {self.numero_nota_fiscal}"

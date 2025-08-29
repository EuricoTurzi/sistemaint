from django.views.generic import ListView, CreateView
from requisicao.models import Requisicoes, Produto, Clientes
from django.shortcuts import get_object_or_404, redirect
from . import models, forms
from .models import Formulario
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from itertools import chain
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from faturamento.models import Faturamento
# Removido import de Clientes pois não é mais necessário   

class FaturamentoListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "faturamento_list.html"
    context_object_name = 'requisicoes'
    paginate_by = 6
    
    permission_required = 'faturamento.view_formulario'  # Substitua 'faturamento' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(status='Reprovado pelo CEO')
        
        # Aplicar ordenação
        ordenacao = self.request.GET.get('ordenacao')
        if ordenacao:
            queryset = queryset.order_by(ordenacao)
        else:
            queryset = queryset.order_by('-id')  # Ordenação padrão por ID em ordem decrescente
        
        # Obter parâmetros dos filtros
        data = self.request.GET.get('data')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        status_faturamento = self.request.GET.get('status_faturamento_filtro')
        cliente = self.request.GET.get('cliente_filtro')
        motivo = self.request.GET.get('motivo_filtro')
        tipo_produto = self.request.GET.get('tipo_produto_filtro')
        contrato_tipo = self.request.GET.get('contrato_tipo_filtro')
        fatura_tipo = self.request.GET.get('fatura_tipo_filtro')
        status = self.request.GET.get('status')
        comercial = self.request.GET.get('comercial')
        cnpj = self.request.GET.get('cnpj')
        busca = self.request.GET.get('busca')
        

        # Aplicar filtros
        if data:
            queryset = queryset.filter(data__date=data)
        elif data_inicio and data_fim:
            queryset = queryset.filter(data__date__range=[data_inicio, data_fim])
        elif data_inicio:
            queryset = queryset.filter(data__date__gte=data_inicio)
        elif data_fim:
            queryset = queryset.filter(data__date__lte=data_fim)
            
        if status_faturamento:
            queryset = queryset.filter(status_faturamento=status_faturamento)
            
        if cliente:
            queryset = queryset.filter(nome_id=cliente)
            
        if motivo:
            queryset = queryset.filter(motivo=motivo)
            
        if tipo_produto:
            queryset = queryset.filter(tipo_produto_id=tipo_produto)
            
        if contrato_tipo:
            queryset = queryset.filter(contrato=contrato_tipo)
            
        if fatura_tipo:
            queryset = queryset.filter(tipo_fatura=fatura_tipo)
            
        if status:
            queryset = queryset.filter(status=status)
            
        if comercial:
            queryset = queryset.filter(comercial=comercial)
            
        if cnpj:
            queryset = queryset.filter(cnpj__icontains=cnpj)
            
        if busca:
            queryset = queryset.filter(nome__nome__icontains=busca)
        

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_faturamento_choices'] = Requisicoes._meta.get_field('status_faturamento').choices
        # Removido clientes_choices pois não é mais necessário
        context['motivo_choices'] = Requisicoes._meta.get_field('motivo').choices
        context['tipo_produto_choices'] = Produto.objects.all()
        context['contrato_tipo_choices'] = Requisicoes._meta.get_field('contrato').choices
        context['fatura_tipo_choices'] = Requisicoes._meta.get_field('tipo_fatura').choices
        context['status_choices'] = Requisicoes._meta.get_field('status').choices
        context['comercial_choices'] = Requisicoes._meta.get_field('comercial').choices
        
        # Manter os filtros aplicados no contexto para a paginação
        context['filtros_aplicados'] = {
            'data': self.request.GET.get('data', ''),
            'data_inicio': self.request.GET.get('data_inicio', ''),
            'data_fim': self.request.GET.get('data_fim', ''),
            'status_faturamento_filtro': self.request.GET.get('status_faturamento_filtro', ''),
            'cliente_filtro': self.request.GET.get('cliente_filtro', ''),
            'motivo_filtro': self.request.GET.get('motivo_filtro', ''),
            'tipo_produto_filtro': self.request.GET.get('tipo_produto_filtro', ''),
            'contrato_tipo_filtro': self.request.GET.get('contrato_tipo_filtro', ''),
            'fatura_tipo_filtro': self.request.GET.get('fatura_tipo_filtro', ''),
            'status': self.request.GET.get('status', ''),
            'comercial': self.request.GET.get('comercial', ''),
            'cnpj': self.request.GET.get('cnpj', ''),
            'busca': self.request.GET.get('busca', ''),
            'ordenacao': self.request.GET.get('ordenacao', ''),
        }
        
        # Adicionar os valores atuais dos filtros para preservar no formulário
        context['current_filters'] = self.request.GET
        
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
        
        # Manter os filtros aplicados no redirecionamento
        params = request.GET.copy()
        if params:
            return redirect(f"{reverse('faturamento_list')}?{params.urlencode()}")
        return redirect('faturamento_list')
    

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




from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class FaturamentoInterativoView(TemplateView):
    template_name = 'faturamento_interativo.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ordenar das mais recentes para as mais antigas (por data de faturamento, depois por ID)
        faturamentos_list = Faturamento.objects.all().order_by('-faturamento', '-id')
        
        # Configurar paginação
        paginator = Paginator(faturamentos_list, 50)  # 50 registros por página
        page = self.request.GET.get('page')
        
        try:
            faturamentos = paginator.page(page)
        except PageNotAnInteger:
            faturamentos = paginator.page(1)
        except EmptyPage:
            faturamentos = paginator.page(paginator.num_pages)
        
        context['faturamentos'] = faturamentos
        context['paginator'] = paginator
        # Removido context['clientes'] pois não é mais necessário
        return context

@method_decorator(csrf_exempt, name='dispatch')
class FaturamentoSaveView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            row_id = data.get('row_id')
            faturamento_data = data.get('data', {})
            
            print(f"Dados recebidos: {faturamento_data}")
            print(f"Row ID: {row_id}")
            
            # Processar campos especiais - cliente é um campo de texto livre
            if 'cliente' in faturamento_data and faturamento_data['cliente']:
                print(f"Cliente digitado: {faturamento_data['cliente']}")
                # O cliente já é uma string, não precisa de processamento especial
            
            # Converter campos vazios para None e processar datas
            print(f"Processando campos antes da conversão: {faturamento_data}")
            
            # Criar um novo dicionário com os campos mapeados corretamente
            processed_data = {}
            
            for field, value in faturamento_data.items():
                # Tratar campos vazios primeiro
                if value == '' or value is None:
                    processed_data[field] = None
                    print(f"Campo {field} convertido para None")
                    continue
                
                # Mapear campos especiais
                mapped_field = field
                if field == 'vecimento':
                    mapped_field = 'vecimento_documento'
                elif field == 'documento':
                    mapped_field = 'tipo_documento'
                
                # Processar campos de data
                if mapped_field in ['faturamento', 'emissao', 'reajuste', 'vecimento_documento', 'data_pgto']:
                    try:
                        from datetime import datetime
                        processed_data[mapped_field] = datetime.strptime(value, '%Y-%m-%d').date()
                    except (ValueError, TypeError):
                        processed_data[mapped_field] = None
                
                # Processar campos decimais
                elif mapped_field in ['valor_bruto', 'coluna1', 'valor_liquido', 'juros', 'valor_pago']:
                    try:
                        from decimal import Decimal
                        processed_data[mapped_field] = Decimal(str(value))
                    except (ValueError, TypeError):
                        processed_data[mapped_field] = None
                
                # Para todos os outros campos, manter o valor como está
                else:
                    processed_data[mapped_field] = value
            
            # Substituir o dicionário original pelo processado
            faturamento_data = processed_data
            
            print(f"Dados finais após processamento: {faturamento_data}")
            
            # Verificar se é uma atualização ou criação
            if isinstance(row_id, int) and row_id > 0:
                # Tentar atualizar registro existente
                try:
                    faturamento = Faturamento.objects.get(id=row_id)
                    print(f"Atualizando registro existente ID: {row_id}")
                    
                    # Atualizar registro existente campo por campo
                    for field, value in faturamento_data.items():
                        if hasattr(faturamento, field):
                            try:
                                setattr(faturamento, field, value)
                                print(f"Campo {field} atualizado para: {value}")
                            except Exception as field_error:
                                print(f"Erro ao atualizar campo {field}: {field_error}")
                                raise field_error
                    
                    faturamento.save()
                    print("Registro existente atualizado com sucesso!")
                    
                except Faturamento.DoesNotExist:
                    # Se não encontrou o registro, criar um novo
                    print(f"Registro ID {row_id} não encontrado, criando novo registro")
                    try:
                        faturamento = Faturamento.objects.create(**faturamento_data)
                        print("Novo registro criado com sucesso!")
                    except Exception as create_error:
                        print(f"Erro específico ao criar: {create_error}")
                        print(f"Dados finais: {faturamento_data}")
                        raise create_error
            else:
                # Criar novo registro (quando row_id é None, 0, ou string vazia)
                print(f"Criando novo registro sem ID com dados: {faturamento_data}")
                try:
                    faturamento = Faturamento.objects.create(**faturamento_data)
                    print("Novo registro criado com sucesso!")
                except Exception as create_error:
                    print(f"Erro específico ao criar: {create_error}")
                    print(f"Dados finais: {faturamento_data}")
                    raise create_error
            
            return JsonResponse({
                'success': True,
                'message': 'Registro salvo com sucesso',
                'id': faturamento.id
            })
            
        except Exception as e:
            print(f"Erro ao salvar faturamento: {str(e)}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class FaturamentoGetDataView(View):
    def get(self, request, *args, **kwargs):
        try:
            from django.db import connection
            
            # Configurar paginação
            page = request.GET.get('page', 1)
            per_page = request.GET.get('per_page', 50)  # 50 registros por página por padrão
            
            try:
                page = int(page)
                per_page = int(per_page)
            except (ValueError, TypeError):
                page = 1
                per_page = 50
            
            # Calcular offset
            offset = (page - 1) * per_page
            
            # Usar raw SQL para evitar problemas de conversão de decimal
            with connection.cursor() as cursor:
                # Primeiro, contar o total de registros
                cursor.execute("""
                    SELECT COUNT(*) FROM faturamento_faturamento
                """)
                total_count = cursor.fetchone()[0]
                
                # Calcular total de páginas
                total_pages = (total_count + per_page - 1) // per_page
                
                # Buscar os registros da página atual
                cursor.execute("""
                    SELECT id, faturamento, emissao, reajustado, reajuste, contrato, tempo, 
                           comercial, n_contrato, sistema_omie, empresa, cliente, nome_fantasia, 
                           email, tipo_servico, descricao, forma_pagamento, vecimento_documento, 
                           tipo_documento, valor_bruto, coluna1, valor_liquido, juros, data_pgto, 
                           valor_pago, status2, situacao
                    FROM faturamento_faturamento 
                    ORDER BY faturamento DESC, id DESC 
                    LIMIT %s OFFSET %s
                """, [per_page, offset])
                
                faturamentos_raw = cursor.fetchall()
            
            data = []
            
            # Função auxiliar para converter valores decimais com segurança
            def safe_float(value):
                if value is None:
                    return None
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return None
            
            # Função auxiliar para converter datas com segurança
            def safe_date(value):
                if value is None:
                    return None
                try:
                    return value.isoformat()
                except:
                    return None
            
            for faturamento_raw in faturamentos_raw:
                try:
                    faturamento_data = {
                        'id': faturamento_raw[0],
                        'faturamento': safe_date(faturamento_raw[1]),
                        'emissao': safe_date(faturamento_raw[2]),
                        'reajustado': faturamento_raw[3],
                        'reajuste': safe_date(faturamento_raw[4]),
                        'contrato': faturamento_raw[5],
                        'tempo': faturamento_raw[6],
                        'comercial': faturamento_raw[7],
                        'n_contrato': faturamento_raw[8],
                        'sistema_omie': faturamento_raw[9],
                        'empresa': faturamento_raw[10],
                        'cliente': faturamento_raw[11] if faturamento_raw[11] else '',
                        'cliente_id': None,  # Não temos mais ID do cliente
                        'nome_fantasia': faturamento_raw[12],
                        'email': faturamento_raw[13],
                        'tipo_servico': faturamento_raw[14],
                        'descricao': faturamento_raw[15],
                        'forma_pagamento': faturamento_raw[16],
                        'vecimento': safe_date(faturamento_raw[17]),
                        'documento': faturamento_raw[18],
                        'valor_bruto': safe_float(faturamento_raw[19]),
                        'coluna1': safe_float(faturamento_raw[20]),
                        'valor_liquido': safe_float(faturamento_raw[21]),
                        'juros': safe_float(faturamento_raw[22]),
                        'data_pgto': safe_date(faturamento_raw[23]),
                        'valor_pago': safe_float(faturamento_raw[24]),
                        'status2': faturamento_raw[25],
                        'situacao': faturamento_raw[26],
                    }
                    data.append(faturamento_data)
                except Exception as e:
                    # Se houver erro ao processar um registro, pular para o próximo
                    continue
            
            return JsonResponse({
                'success': True,
                'faturamentos': data,
                'pagination': {
                    'current_page': page,
                    'total_pages': total_pages,
                    'total_records': total_count,
                    'has_previous': page > 1,
                    'has_next': page < total_pages,
                    'previous_page_number': page - 1 if page > 1 else None,
                    'next_page_number': page + 1 if page < total_pages else None,
                    'per_page': per_page
                }
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class FaturamentoDeleteView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            row_id = data.get('row_id')
            
            if row_id:
                try:
                    faturamento = Faturamento.objects.get(id=row_id)
                    faturamento.delete()
                    return JsonResponse({
                        'success': True,
                        'message': 'Registro deletado com sucesso'
                    })
                except Faturamento.DoesNotExist:
                    return JsonResponse({
                        'success': False,
                        'error': 'Registro não encontrado'
                    }, status=404)
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'ID do registro não fornecido'
                }, status=400)
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400) 
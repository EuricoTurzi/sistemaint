from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from requisicao.models import Requisicoes
import requests
from datetime import datetime, timedelta
from django.utils import timezone
import json
import pickle
import os
from django.conf import settings

class RequisicoesDescartavelListView(LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = 'corte/listar_requisicoes_descartavel.html'
    context_object_name = 'requisicoes'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtra apenas requisições com contrato "Descartavel"
        queryset = queryset.filter(contrato='Descartavel')
        
        # Recupera parâmetros de busca
        id_equipamento = self.request.GET.get('id_equipamento')
        iccid = self.request.GET.get('iccid')
        cliente = self.request.GET.get('cliente')
        status = self.request.GET.get('status')
        
        # Aplica filtros adicionais se fornecidos
        if id_equipamento:
            queryset = queryset.filter(id_equipamentos__icontains=id_equipamento.strip())
        
        if iccid:
            queryset = queryset.filter(iccid__icontains=iccid.strip())
            
        if cliente:
            queryset = queryset.filter(nome__nome__icontains=cliente.strip())
            
        if status:
            queryset = queryset.filter(status__icontains=status.strip())
        
        # Ordena por data da requisição (mais recentes primeiro)
        return queryset.order_by('-data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Adiciona filtros ao contexto
        context['id_equipamento_filter'] = self.request.GET.get('id_equipamento', '')
        context['iccid_filter'] = self.request.GET.get('iccid', '')
        context['cliente_filter'] = self.request.GET.get('cliente', '')
        context['status_filter'] = self.request.GET.get('status', '')
        
        # Adiciona data atual para cálculos no template
        context['data_atual'] = timezone.now()
        
        # Adiciona total de requisições
        context['total_requisicoes'] = self.get_queryset().count()
        
        # Busca equipamentos da API
        equipamentos_api_data = self.get_equipamentos_aptos_corte()
        
        # Verifica se os dados vieram do cache
        cache_data = self.load_cache()
        dados_do_cache = bool(cache_data)
        
        context['equipamentos_aptos_corte'] = equipamentos_api_data.get('aptos_corte', {})
        context['todos_equipamentos_api'] = equipamentos_api_data.get('todos_equipamentos', {})
        context['total_equipamentos_aptos'] = len(equipamentos_api_data.get('aptos_corte', {}))
        context['cache_data'] = dados_do_cache
        
        return context

    def get_cache_file_path(self):
        """Retorna o caminho do arquivo de cache"""
        cache_dir = os.path.join(settings.BASE_DIR, 'cache')
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        return os.path.join(cache_dir, 'stc_api_cache.pkl')

    def load_cache(self):
        """Carrega dados do cache se existir e não estiver expirado"""
        cache_file = self.get_cache_file_path()
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'rb') as f:
                    cache_data = pickle.load(f)
                
                # Verifica se o cache não expirou (5 minutos)
                if cache_data.get('timestamp') and (timezone.now() - cache_data['timestamp']).total_seconds() < 300:
                    print("=" * 80)
                    print("USANDO DADOS DO CACHE (não expirado)")
                    print(f"Cache criado em: {cache_data['timestamp']}")
                    print("=" * 80)
                    return cache_data.get('data', {})
            except Exception as e:
                print(f"Erro ao carregar cache: {e}")
        return None

    def save_cache(self, data):
        """Salva dados no cache"""
        try:
            cache_file = self.get_cache_file_path()
            cache_data = {
                'timestamp': timezone.now(),
                'data': data
            }
            with open(cache_file, 'wb') as f:
                pickle.dump(cache_data, f)
            print("=" * 80)
            print("DADOS SALVOS NO CACHE")
            print(f"Cache salvo em: {cache_file}")
            print("=" * 80)
        except Exception as e:
            print(f"Erro ao salvar cache: {e}")

    def get_equipamentos_aptos_corte(self):
        """
        Busca equipamentos da API da STC e calcula apto ao corte baseado na diferença
        entre primeira e última posição (se > 30 dias = apto ao corte)
        """
        try:
            # Tenta carregar do cache primeiro
            cache_data = self.load_cache()
            if cache_data:
                print("Dados carregados do cache")
                return cache_data
            
            # Se não há cache, faz a requisição para a API
            url = "http://ap3.stc.srv.br/integration/prod/ws/getClientVehicles"
            body = {
                "key": "d548f2c076480dcc2bd69fcbf8e6be61",
                "user": "controle.descártavel",
                "pass": "51d834cff9ee007ed1dc9366335dc0da"
            }
            
            print(f"Fazendo requisição para: {url}")
            print(f"Body: {body}")
            
            response = requests.post(url, json=body, timeout=30)
            print(f"Status da resposta: {response.status_code}")
            
            if response.status_code == 200:
                api_data = response.json()
                print("Resposta da API recebida:")
                print(json.dumps(api_data, indent=2, ensure_ascii=False))
                
                # Verifica se a resposta foi bem-sucedida
                if not api_data.get('success', False):
                    error_msg = api_data.get('msg', 'Erro desconhecido')
                    print(f"API retornou erro: {error_msg}")
                    
                    # Se atingiu limite de acessos, tenta carregar cache antigo
                    if "Limite de acessos" in error_msg:
                        print("Limite de acessos atingido, tentando carregar cache antigo...")
                        old_cache = self.load_old_cache()
                        if old_cache:
                            print("Cache antigo carregado com sucesso")
                            return old_cache
                    
                    return {'aptos_corte': {}, 'todos_equipamentos': {}}
                
                # Extrai a lista de equipamentos
                equipamentos_lista = api_data.get('data', [])
                print(f"Total de equipamentos na API: {len(equipamentos_lista)}")
                
                todos_equipamentos = {}
                equipamentos_aptos = {}
                
                # Agrupa posições por deviceId para calcular primeira e última
                posicoes_por_equipamento = {}
                
                for equipamento in equipamentos_lista:
                    device_id = equipamento.get('deviceId')
                    if not device_id:
                        continue
                    
                    # Converte data para datetime para comparação
                    try:
                        data_posicao = datetime.strptime(equipamento.get('date', ''), '%Y-%m-%d %H:%M:%S')
                        equipamento['data_posicao_dt'] = data_posicao
                    except:
                        continue
                    
                    if device_id not in posicoes_por_equipamento:
                        posicoes_por_equipamento[device_id] = []
                    
                    posicoes_por_equipamento[device_id].append(equipamento)
                
                # Para cada equipamento, calcula primeira e última posição
                for device_id, posicoes in posicoes_por_equipamento.items():
                    print(f"Processando equipamento {device_id} com {len(posicoes)} posições")
                    
                    # Ordena posições por data
                    posicoes_ordenadas = sorted(posicoes, key=lambda x: x['data_posicao_dt'])
                    
                    primeira_posicao = posicoes_ordenadas[0]
                    ultima_posicao = posicoes_ordenadas[-1]
                    
                    print(f"  Primeira posição: {primeira_posicao.get('date')}")
                    print(f"  Última posição: {ultima_posicao.get('date')}")
                    
                    # Calcula diferença em dias (se houver mais de uma posição)
                    if len(posicoes) > 1:
                        diferenca_dias = (ultima_posicao['data_posicao_dt'] - primeira_posicao['data_posicao_dt']).days
                        print(f"  Diferença entre posições: {diferenca_dias} dias")
                    else:
                        diferenca_dias = 0
                        print(f"  Apenas uma posição - não pode calcular diferença entre posições")
                    
                    # Determina se está apto ao corte baseado em duas regras:
                    apto_ao_corte = False
                    motivo_apto_corte = ""
                    
                    # Regra 1: Diferença entre primeira e última posição > 30 dias
                    if len(posicoes) > 1 and diferenca_dias > 30:
                        apto_ao_corte = True
                        motivo_apto_corte = f"Diferença entre posições: {diferenca_dias} dias > 30 dias"
                        print(f"  APTO AO CORTE - Regra 1: {motivo_apto_corte}")
                    
                    # Regra 2: Data da posição mais recente > 6 meses da data da requisição
                    # (Esta verificação será feita no template para cada requisição específica)
                    
                    # Prepara dados do equipamento
                    equipamento_info = {
                        'positionId': ultima_posicao.get('positionId'),
                        'date': ultima_posicao.get('date'),
                        'deviceId': device_id,
                        'latitude': ultima_posicao.get('latitude'),
                        'longitude': ultima_posicao.get('longitude'),
                        'endereco': ultima_posicao.get('address'),
                        'velocidade': ultima_posicao.get('speed'),
                        'direcao': ultima_posicao.get('direction'),
                        'status_equipamento': ultima_posicao.get('ignition'),
                        'data_ultima_posicao': ultima_posicao.get('date'),
                        'ultima_posicao': f"Lat: {ultima_posicao.get('latitude')}, Long: {ultima_posicao.get('longitude')}",
                        'vehicleId': ultima_posicao.get('vehicleId'),
                        'plate': ultima_posicao.get('plate'),
                        'deviceModel': ultima_posicao.get('deviceModel'),
                        'ignition': ultima_posicao.get('ignition'),
                        'speed': ultima_posicao.get('speed'),
                        'direction': ultima_posicao.get('direction'),
                        'address': ultima_posicao.get('address'),
                        
                        # Novos campos para primeira e última posição
                        'primeira_posicao': primeira_posicao,
                        'ultima_posicao_detalhada': ultima_posicao,
                        'data_primeira_posicao': primeira_posicao.get('date'),
                        'data_ultima_posicao_detalhada': ultima_posicao.get('date'),
                        'diferenca_dias': diferenca_dias,
                        'apto_ao_corte': apto_ao_corte,
                        'motivo_apto_corte': motivo_apto_corte,
                        'total_posicoes': len(posicoes)
                    }
                    
                    todos_equipamentos[device_id] = equipamento_info
                    print(f"  Equipamento {device_id} adicionado aos todos_equipamentos")
                    
                    # Se está apto ao corte, adiciona à lista de aptos
                    if apto_ao_corte:
                        equipamentos_aptos[device_id] = equipamento_info
                        print(f"  Equipamento {device_id} adicionado aos aptos ao corte")
                
                print(f"Equipamentos processados: {len(todos_equipamentos)}")
                print(f"Equipamentos aptos ao corte: {len(equipamentos_aptos)}")
                
                # Debug: mostra todos os equipamentos processados
                for device_id, info in todos_equipamentos.items():
                    print(f"  {device_id}: {info.get('plate')} - {info.get('diferenca_dias')} dias - Apto: {info.get('apto_ao_corte')}")
                
                # Salva no cache
                result = {'aptos_corte': equipamentos_aptos, 'todos_equipamentos': todos_equipamentos}
                self.save_cache(result)
                
                return result
                
            else:
                print(f"Erro na requisição: {response.status_code}")
                print(f"Resposta: {response.text}")
                
                # Tenta carregar cache antigo em caso de erro
                old_cache = self.load_old_cache()
                if old_cache:
                    print("Cache antigo carregado devido ao erro")
                    return old_cache
                
                return {'aptos_corte': {}, 'todos_equipamentos': {}}
                
        except Exception as e:
            print(f"Erro ao buscar equipamentos: {str(e)}")
            
            # Tenta carregar cache antigo em caso de erro
            old_cache = self.load_old_cache()
            if old_cache:
                print("Cache antigo carregado devido ao erro")
                return old_cache
            
            return {'aptos_corte': {}, 'todos_equipamentos': {}}

    def load_old_cache(self):
        """Carrega cache antigo mesmo se expirado"""
        cache_file = self.get_cache_file_path()
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'rb') as f:
                    cache_data = pickle.load(f)
                print(f"Cache antigo encontrado de: {cache_data.get('timestamp')}")
                return cache_data.get('data', {})
            except Exception as e:
                print(f"Erro ao carregar cache antigo: {e}")
        return None

    def calcular_apto_corte_por_requisicao(self, equipamentos_api, requisicao):
        """
        Calcula se um equipamento está apto ao corte baseado na data da requisição
        """
        if not requisicao.data or not equipamentos_api:
            return {}
        
        equipamentos_aptos = {}
        data_requisicao = requisicao.data
        
        for device_id, equipamento in equipamentos_api.items():
            if requisicao.id_equipamentos and str(device_id) in str(requisicao.id_equipamentos):
                try:
                    # Converte a data da API para datetime
                    date_str = equipamento.get('date')
                    data_equipamento = None
                    
                    for formato in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y']:
                        try:
                            data_equipamento = datetime.strptime(date_str, formato)
                            break
                        except ValueError:
                            continue
                    
                    if data_equipamento:
                        # Calcula 30 dias após a data da requisição (não da API)
                        data_limite = data_requisicao + timedelta(days=30)
                        dias_atraso = (timezone.now().date() - data_limite.date()).days
                        
                        # Atualiza os dados do equipamento
                        equipamento['data_limite'] = data_limite.strftime('%d/%m/%Y')
                        equipamento['dias_atraso'] = dias_atraso
                        
                        # Se passou dos 30 dias, está apto ao corte
                        if dias_atraso > 0:
                            equipamentos_aptos[device_id] = equipamento
                            print(f"Equipamento {device_id} apto ao corte: {dias_atraso} dias de atraso")
                
                except Exception as e:
                    print(f"Erro ao calcular apto ao corte para equipamento {device_id}: {e}")
                    continue
        
        return equipamentos_aptos 
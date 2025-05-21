from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import RegistroPagamento, Formacompanhamento, agentes
from .forms import RegistroPagamentoForm, formacompanhamentoForm, agentesForm
from .utils import generate_pdf
import json

# ----------------- Forma de Acompanhamento -----------------

class formulariorateview(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Formacompanhamento
    template_name = 'formacompanhamento.html'
    form_class = formacompanhamentoForm
    context_object_name = 'acomp'
    success_url = reverse_lazy('formacompanhamento')
    permission_required = 'formacompanhamento.add_formacompanhamento'


class AcompanhamentoListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Formacompanhamento
    template_name = 'facomp.html'
    context_object_name = 'acomp'
    permission_required = 'formacompanhamento.view_formacompanhamento'


class formListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Formacompanhamento
    template_name = 'formacompanhamento_detail.html'
    context_object_name = 'acompanhamento'
    permission_required = 'formacompanhamento.view_formacompanhamento'


# ----------------- Agentes -----------------

class agenteCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = agentes
    template_name = 'agentes_create.html'
    form_class = agentesForm
    context_object_name = 'agentes'
    success_url = reverse_lazy('agenteCreateView')
    permission_required = 'formacompanhamento.add_agentes'


class AgentesListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = agentes
    template_name = 'agentes_list.html'
    context_object_name = 'agente'
    permission_required = 'formacompanhamento.view_agentes'


class agenteUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = agentes
    template_name = 'agente_update.html'
    form_class = agentesForm
    success_url = reverse_lazy('agentesListView')
    permission_required = "formacompanhamento.view_agentes"


def get_agente_data(request, agente_id):
    agente = get_object_or_404(agentes, id=agente_id)
    data = {
        'placa': agente.placa,
    }
    return JsonResponse(data)


# ----------------- Registro de Pagamento -----------------
from django.views.generic import ListView
from formacompanhamento.models import RegistroPagamento


class RegistroPagamentoListView(ListView):
    model = RegistroPagamento
    template_name = 'registro_pagamento_list.html'
    context_object_name = 'registros'
    paginate_by = 10
    ordering = ['-data_hora_inicial']

    def get_queryset(self):
        queryset = super().get_queryset()
        for registro in queryset:
            # Adicionar atributos calculados dinamicamente
            registro.hora_total = registro.calcular_hora_total()
            registro.valor_total_hora_excedente = registro.calcular_valor_total_hora_excedente()
            registro.km_total = registro.calcular_km_total()
            registro.km_excedente = registro.calcular_km_excedente()
            registro.valor_total_km_excedente = registro.calcular_valor_total_km_excedente()
            registro.total_acionamento = registro.calcular_total_acionamento()
        return queryset



from datetime import timedelta
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import RegistroPagamento
from .forms import RegistroPagamentoForm
import logging

logger = logging.getLogger(__name__)

class RegistroPagamentoCreateView(CreateView):
    model = RegistroPagamento
    form_class = RegistroPagamentoForm
    template_name = 'registro_pagamento_form.html'
    success_url = reverse_lazy('formacompanhamento:registro_pagamento_list')

    def form_valid(self, form):
        instance = form.save(commit=False)

        # Preenchendo previsa_chegada com base em data_hora_inicial e sla
        if instance.data_hora_inicial and instance.sla:
            try:
                if isinstance(instance.sla, timedelta):
                    # Caso sla seja um timedelta, soma diretamente
                    instance.previsa_chegada = instance.data_hora_inicial + instance.sla
                else:
                    # Caso sla seja um inteiro ou string representando minutos
                    instance.previsa_chegada = instance.data_hora_inicial + timedelta(minutes=int(instance.sla))
            except (ValueError, TypeError) as e:
                logger.error(f"Erro ao calcular previsa_chegada: {e}")
                instance.previsa_chegada = None

        # Calculando hora_total (em horas)
        if instance.data_hora_inicial and instance.data_hora_final:
            try:
                duration = instance.data_hora_final - instance.data_hora_inicial
                instance.hora_total = round(duration.total_seconds() / 3600, 2)  # Total em horas
            except Exception as e:
                logger.error(f"Erro ao calcular hora_total: {e}")
                instance.hora_total = 0

        # Calculando km_total e km_excedente
        if instance.km_inicial is not None and instance.km_final is not None:
            try:
                instance.km_total = max(instance.km_final - instance.km_inicial, 0)
                if instance.km_franquia is not None:
                    instance.km_excedente = max(instance.km_total - instance.km_franquia, 0)
                else:
                    instance.km_excedente = 0
            except Exception as e:
                logger.error(f"Erro ao calcular km_total ou km_excedente: {e}")
                instance.km_total = 0
                instance.km_excedente = 0

        # Salvando a instância no banco de dados
        try:
            instance.save()
            logger.info(f"Registro criado com sucesso: {instance.id}")
        except Exception as e:
            logger.error(f"Erro ao salvar o registro no banco de dados: {e}")
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        # Log para depuração dos erros
        logger.error("Erro ao validar o formulário:")
        for field, errors in form.errors.items():
            logger.error(f"{field}: {errors}")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_range'] = range(1, 17)  # De 1 a 16
        return context


# Função auxiliar para buscar dados do prestador
def get_prestador_data(request):
    prestador_id = request.GET.get('prestador_id')
    if not prestador_id:
        return JsonResponse({'error': 'ID do prestador não fornecido'}, status=400)

    try:
        prestador = prestadores.objects.get(pk=prestador_id)
        data = {
            'valor_acionamento': str(prestador.valor_acionamento),
            'franquia_hora': prestador.franquia_hora,
            'km_franquia': str(prestador.franquia_km),
            'valorkm': str(prestador.valorkm),  # Incluindo valorkm
            'valorh': str(prestador.valorh)     # Incluindo valorh
        }
        return JsonResponse(data)
    except prestadores.DoesNotExist:
        return JsonResponse({'error': 'Prestador não encontrado'}, status=404)


from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import RegistroPagamento
from .forms import RegistroPagamentoForm
from .models import clientes_acionamento


class RegistroPagamentoUpdateView(UpdateView):
    model = RegistroPagamento
    form_class = RegistroPagamentoForm
    template_name = 'registro_pagamento_update.html'  # Seu template de edição
    success_url = reverse_lazy('formacompanhamento:registro_pagamento_list')  # Redireciona após salvar

    def form_valid(self, form):
        return super().form_valid(form)




from django.views.generic.edit import UpdateView
from .models import clientes_acionamento
from .forms import ClientesAcionamentoForm
from django.urls import reverse_lazy

class ClienteUpdateView(UpdateView):
    model = clientes_acionamento
    form_class = ClientesAcionamentoForm
    template_name = 'update_clientes_acionamento.html'
    success_url = reverse_lazy('formacompanhamento:clientes_acionamento_list')



class RegistroPagamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistroPagamento
    template_name = 'registro_pagamento_confirm_delete.html'
    success_url = reverse_lazy('registro_pagamento_list')


def validar(request, pk):
    registro = get_object_or_404(RegistroPagamento, pk=pk)
    registro.status = "A Faturar"  # Atualize o status do registro
    registro.save()
    return redirect('formacompanhamento:registro_pagamento_list')


# ----------------- Atualização de Registro -----------------
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from formacompanhamento.models import Registro

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Registro, clientes_acionamento
from django.shortcuts import render, redirect
from .models import Registro, clientes_acionamento
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def nova_tabela_view(request):
    """
    View para renderizar a tabela com os registros existentes e carregar os clientes.
    Também permite criar novos registros via formulário.
    """
    registros = Registro.objects.all()  # Busca todos os registros
    clientes = clientes_acionamento.objects.all()  # Busca todos os clientes

    if request.method == "POST":
        form = RegistroPagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nova_tabela')  # Redireciona para a mesma página após salvar
    else:
        form = RegistroPagamentoForm()

    return render(request, 'nova_tabela.html', {
        'registros': registros,
        'clientes': clientes,
        'form': form  # Formulário para criar um novo registro
    })


@csrf_exempt
def atualizar_registro(request):
    """
    View para atualizar os registros via requisição AJAX.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Dados recebidos no backend:", data)  # Log para depuração

            registro_id = data.get('id')
            if not registro_id:
                return JsonResponse({'error': 'ID é obrigatório.'}, status=400)

            # Recupera o registro no banco de dados
            registro = Registro.objects.filter(id=registro_id).first()
            if not registro:
                return JsonResponse({'error': 'Registro não encontrado.'}, status=404)

            # Atualiza os campos do registro
            registro.hora_excedente = data.get('hora_excedente', registro.hora_excedente)
            registro.valor_hora_excedente = data.get('valor_hora_excedente', registro.valor_hora_excedente)
            registro.km_excedente = data.get('km_excedente', registro.km_excedente)
            registro.valor_km_excedente = data.get('valor_km_excedente', registro.valor_km_excedente)
            registro.acionamento = data.get('acionamento', registro.acionamento)
            registro.total_cliente = data.get('total_cliente', registro.total_cliente)
            registro.save()  # Salva no banco

            return JsonResponse({'message': 'Registro atualizado com sucesso!'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            print("Erro no backend:", str(e))  # Log para depuração
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido.'}, status=405)




def download_pdf(request, pk):
    registro = get_object_or_404(RegistroPagamento, pk=pk)
    pdf = generate_pdf(registro)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="registro_pagamento_{registro.id}.pdf"'
    return response


# ----------------- Nova Tabela -----------------









from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import RegistroPagamentoForm
from .models import RegistroPagamento
from .utils import generate_pdf  # Certifique-se de que esta função existe

class FormularioView(FormView):
    template_name = "registro_pagamento_form.html"  # Altere para o template correto do formulário
    form_class = RegistroPagamentoForm

    def form_valid(self, form):
        # Salva o formulário no banco de dados e cria uma instância
        instance = form.save()

        # Gera o PDF com os dados do registro salvo
        pdf = generate_pdf(instance)

        # Verifica se o PDF foi gerado corretamente
        if not pdf:
            return HttpResponse("Erro ao gerar o PDF.", status=500)

        # Retorna o PDF como resposta para download
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="relatorio_{instance.id}.pdf"'
        return response








from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import prestadores
from .forms import PrestadoresForm

from django.http import HttpResponseNotAllowed
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import prestadores
from .forms import PrestadoresForm

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed
from .models import prestadores
from .forms import PrestadoresForm
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
import logging
from .models import prestadores
from .forms import PrestadoresForm

from django.contrib import messages

class PrestadorCreateView(CreateView):
    model = prestadores
    form_class = PrestadoresForm
    template_name = 'formulario_prestador.html'
    success_url = reverse_lazy('formacompanhamento:lista_prestadores')

    def form_valid(self, form):
        try:
            # Salva o novo prestador
            response = super().form_valid(form)
            message = f"Prestador {form.instance.Nome} criado com sucesso (ID: {form.instance.id})"
            # Adiciona a mensagem de sucesso
            messages.success(self.request, message)
            return response
        except Exception as e:
            # Caso ocorra algum erro, loga a exceção
            message = f"Erro ao criar o prestador: {e}"
            messages.error(self.request, message)
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        print("Erros do Formulário:", form.errors)  # Debug para ver o que está errado
        messages.error(self.request, f"Formulário inválido. Erros: {form.errors}")
        return super().form_invalid(form)



from django.views.generic import ListView
from django.db.models import Q
from .models import prestadores

class PrestadorListView(ListView):
    model = prestadores
    template_name = 'lista_prestadores.html'
    context_object_name = 'prestadores'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        disponibilidade = self.request.GET.get('disponibilidade', '').strip()
        regiao_atuacao = self.request.GET.get('regiao_atuacao', '').strip()
        status = self.request.GET.get('status', '').strip()

        # Aplica os filtros somente se houver valores nos campos
        if query:
            queryset = queryset.filter(Nome__icontains=query)  # __icontains para busca case-insensitive
        if disponibilidade:
            queryset = queryset.filter(disponibilidade__icontains=disponibilidade)  # __icontains
        if regiao_atuacao:
            queryset = queryset.filter(regiao_atuacao__icontains=regiao_atuacao)  # __icontains
        if status:
            queryset = queryset.filter(status_prestador__iexact=status)  # __iexact é para igualdade exata, mas case-insensitive

        return queryset



    from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import clientes_acionamento
from .forms import ClientesAcionamentoForm
from .forms import ClientesAcionamentoForm


class ClientesAcionamentoCreateView(CreateView):
    model = clientes_acionamento
    form_class = ClientesAcionamentoForm
    template_name = 'create_clientes_acionamento.html'
    success_url = reverse_lazy('formacompanhamento:clientes_acionamento_list')
  # Substitua pelo nome da URL de listagem, se necessário

from django.views.generic import ListView


class ClientesAcionamentoListView(ListView):
    model = clientes_acionamento
    template_name = 'clientes_acionamento_list.html'
    context_object_name = 'clientes'

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .utils import generate_pdf
from .models import RegistroPagamento
import logging

logger = logging.getLogger(__name__)

def download_pdf(request, instance_id):
    """
    Gera e retorna o PDF para download com base na instância do RegistroPagamento.
    """
    registro = get_object_or_404(RegistroPagamento, pk=instance_id)

    try:
        # Gera o PDF
        pdf = generate_pdf(registro)
    except Exception as e:
        logger.error(f"Erro ao gerar PDF para o registro {instance_id}: {e}")
        return HttpResponse("Erro ao gerar o PDF.", status=500)

    # Configura a resposta HTTP para download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="registro_pagamento_{registro.id}.pdf"'
    return response


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import RegistroPagamento

def obter_dados_registro(request, registro_id):
    registro = get_object_or_404(RegistroPagamento, id=registro_id)
    dados = {
        "total_acionamento": float(registro.calcular_total_acionamento()),
        "km_excedente": float(registro.calcular_km_excedente()),
        "hora_excedente": float(registro.calcular_hora_excedente()),
    }
    return JsonResponse(dados)

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from .models import RegistroPagamento, clientes_acionamento, TotalRegistro
from django.http import HttpResponse

class TotalFormView(TemplateView):
    template_name = 'total.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registros'] = RegistroPagamento.objects.all()
        context['clientes'] = clientes_acionamento.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        registro_id = request.GET.get('registro_id')
        if registro_id:
            registro = get_object_or_404(RegistroPagamento, id=registro_id)
            return JsonResponse({
                "total_acionamento": float(registro.total_acionamento),
                "km_excedente": float(registro.km_excedente),
                "hora_excedente": float(registro.hora_excedente),
                "valor_km_excedente": float(registro.valor_total_km_excedente),
                "valor_hora_excedente": float(registro.calcular_valor_total_hora_excedente()),
            })
        return super().get(request, *args, **kwargs)
        



from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import RegistroPagamento  # Ajuste conforme o nome do modelo


def registro_dados(request, registro_id):
    """
    Retorna os dados do registro em JSON.
    """
    registro = get_object_or_404(RegistroPagamento, id=registro_id)

    # Garantir que os valores são calculados ao acessar
    registro.save()  # Força a reexecução do cálculo

    dados = {
        "total_acionamento": float(registro.total_acionamento or 0.0),
        "km_excedente": float(registro.km_excedente or 0.0),
        "hora_excedente": float(registro.hora_excedente or 0.0),
    }

    return JsonResponse(dados)


from django.http import JsonResponse, Http404

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import clientes_acionamento


def obter_dados_cliente(request, cliente_id):
    """
    Retorna os dados do cliente em JSON.
    """
    cliente = get_object_or_404(clientes_acionamento, id=cliente_id)

    dados = {
        "franquia_km": float(cliente.franquiakm or 0),
        "franquia_hora": float(cliente.franquiahora or 0),
        "valor_acionamento": float(cliente.valordeacionamento or 0),  # ✅ Corrigido aqui!
        "valor_km": float(cliente.valor_km or 0),
        "valor_hora": float(cliente.valor_hora or 0),
    }
    return JsonResponse(dados)

from django.shortcuts import render
from .models import RegistroPagamento, clientes_acionamento

# views.py




from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import RegistroPagamento, clientes_acionamento

from django.views.generic import TemplateView
from .models import clientes_acionamento, RegistroPagamento

class TabelaRegistrosView(TemplateView):
    template_name = 'tabela_registros.html'  # Nome do template a ser renderizado
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar dados do primeiro modelo
        context['registros'] = TotalRegistro.objects.all()

        

        return context


        

class prestadoresupdate(UpdateView):
    model = prestadores
    form_class = PrestadoresForm
    context_object_name = 'prestadores'
    template_name = 'prestadores_update.html'
    success_url = reverse_lazy('formacompanhamento:lista_prestadores')

# projetos/views.py

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Registro
from .forms import RegistroForm

class CriarRegistroView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View para criar um novo registro.
    Apenas usuários autenticados com a permissão 'projetos.add_registro' podem acessar.
    """
    model = Registro
    form_class = RegistroForm
    template_name = 'criar_registro.html'
    permission_required = 'projetos.add_registro'
    raise_exception = True  # Levanta uma exceção 403 se a permissão não for atendida

    def form_valid(self, form):
        """
        Sobrescreve o método form_valid para associar o registro ao usuário que está criando.
        """
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redireciona para a lista de registros após a criação bem-sucedida.
        """
        return reverse_lazy('listar_registros')


class ListarRegistrosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View para listar todos os registros.
    Apenas usuários autenticados com a permissão 'projetos.view_registro' podem acessar.
    """
    model = Registro
    template_name = 'listar_registros.html'
    context_object_name = 'registros'
    permission_required = 'projetos.view_registro'
    raise_exception = True  # Levanta uma exceção 403 se a permissão não for atendida


class DashboardView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """
    View para exibir o dashboard com estatísticas dos registros.
    Apenas usuários autenticados com a permissão 'projetos.view_registro' podem acessar.
    """
    template_name = 'dashboard.html'
    permission_required = 'projetos.view_registro'
    raise_exception = True  # Levanta uma exceção 403 se a permissão não for atendida

    def get_context_data(self, **kwargs):
        """
        Adiciona dados contextuais para o dashboard.
        """
        context = super().get_context_data(**kwargs)
        registros = Registro.objects.all()
        context['total_insercoes'] = registros.count()

        # Inserções por usuário
        insercoes_por_usuario = registros.values('usuario__username').annotate(total=Count('id')).order_by('-total')
        context['usuarios_labels'] = [item['usuario__username'] for item in insercoes_por_usuario]
        context['usuarios_data'] = [item['total'] for item in insercoes_por_usuario]

        # Inserções por local
        insercoes_por_local = registros.values('local').annotate(total=Count('id')).order_by('-total')
        context['locais_labels'] = [item['local'] for item in insercoes_por_local]
        context['locais_data'] = [item['total'] for item in insercoes_por_local]

        # Inserções por data
        insercoes_por_data = registros.extra(select={'data': "DATE(data_insercao)"}).values('data').annotate(total=Count('id')).order_by('data')
        context['datas_labels'] = [item['data'] for item in insercoes_por_data]
        context['datas_data'] = [item['total'] for item in insercoes_por_data]

        # Inserções por operação
        insercoes_por_operacao = registros.values('operacao').annotate(total=Count('id')).order_by('-total')
        context['operacoes_labels'] = [item['operacao'] for item in insercoes_por_operacao]
        context['operacoes_data'] = [item['total'] for item in insercoes_por_operacao]

        return context

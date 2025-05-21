from django.views.generic import TemplateView
from django.db.models import Sum
from requisicao.models import Requisicoes
from cliente.models import Cliente
from produto.models import Produto
from registrodemanutencao.models import registrodemanutencao
from reativacao.models import Reativacao  # Certifique-se de importar o modelo Reativacao
from .models import Log


class AdminDashboardView(TemplateView):
    template_name = 'admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requisicoes_count'] = Requisicoes.objects.count()
        context['clientes_count'] = Cliente.objects.count()
        context['produtos_count'] = Produto.objects.count()
        context['manutencoes_count'] = registrodemanutencao.objects.count()
        valor_total_vendas = Requisicoes.objects.aggregate(total=Sum('valor_total'))['total'] or 0
        context['valor_total_vendas'] = f"R$ {valor_total_vendas:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        context['reativacoes_count'] = Reativacao.objects.count()
        context['logs'] = Log.objects.all().order_by('-timestamp')[:10]  # Mostra os 10 logs mais recentes
        return context
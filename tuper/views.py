from django.urls import path
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Transportadora, formulario_divisao, estoque_tuper
from .forms import TransportadoraForm, TransregistroForm, EstoqueTuperForm

class RegistrarTransportadoraView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Transportadora
    form_class = TransportadoraForm
    template_name = 'registro_transportadora.html'
    success_url = reverse_lazy('registrar_transportadora')
    permission_required = 'tuper.add_transportadora'

class DivisaoIscasView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = formulario_divisao
    form_class = TransregistroForm
    template_name = 'divisao_iscas.html'
    success_url = reverse_lazy('divisao_iscas')
    permission_required = 'tuper.add_formulario_divisao'

class RegistrarEstoqueView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = estoque_tuper
    form_class = EstoqueTuperForm
    template_name = 'registro_estoque.html'
    success_url = reverse_lazy('registrar_estoque')
    permission_required = 'tuper.add_estoque_tuper'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estoques'] = estoque_tuper.objects.all()
        return context
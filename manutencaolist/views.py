from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import manutensaolis
from registrodemanutencao.forms import FormulariosForm, FormulariosUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class FormulariosCreateView( PermissionRequiredMixin,LoginRequiredMixin,  CreateView):
    model = manutensaolis
    form_class = FormulariosForm
    template_name = 'manutencaocreate.html'
    success_url = reverse_lazy('manutencao')
    permission_required = 'manutencaolist.add_manutensaolis'  # Substitua 'manutencaolist' pelo nome do seu aplicativo

from django.db import transaction

class FormulariosUpdateView( PermissionRequiredMixin,LoginRequiredMixin,  UpdateView):
    model = manutensaolis
    form_class = FormulariosUpdateForm
    template_name = 'manutencaoup.html'
    success_url = reverse_lazy('registrodemanutencao')
    permission_required = 'manutencaolist.change_manutensaolis'  # Substitua 'manutencaolist' pelo nome do seu aplicativo

class FormularioListView( PermissionRequiredMixin,LoginRequiredMixin,  ListView):
    model = manutensaolis
    template_name = "manutencaolist.html"
    context_object_name = 'registrodemanutencao'
    paginate_by = 6
    permission_required = 'manutencaolist.view_manutensaolis'  # Substitua 'manutencaolist' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        status = self.request.GET.get('status')
        faturamento = self.request.GET.get('faturamento')

        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        if status:
            queryset = queryset.filter(status=status)
        if faturamento:
            queryset = queryset.filter(faturamento=faturamento)

        return queryset

class FormularioDetailView( PermissionRequiredMixin,LoginRequiredMixin,  DetailView):
    model = manutensaolis
    template_name = 'manutencaodetail.html'
    context_object_name = 'registrodemanutencao_detail'
    permission_required = 'manutencaolist.view_manutensaolis'  # Substitua 'manutencaolist' pelo nome do seu aplicativo

class FormularioDeleteView( PermissionRequiredMixin,LoginRequiredMixin,  DeleteView):
    model = manutensaolis
    template_name = 'manutencaodelete.html'
    success_url = reverse_lazy('registrodemanutencaolist')
    permission_required = 'manutencaolist.delete_manutensaolis'  # Substitua 'manutencaolist' pelo nome do seu aplicativo

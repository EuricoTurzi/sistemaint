from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Qualit
from .forms import QualitForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class QualitCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Qualit
    form_class = QualitForm
    template_name = 'criar_qualit.html'
    success_url = reverse_lazy('criar_qualit')
    permission_required = 'qualit.add_qualit'  # Substitua 'qualit' pelo nome do seu aplicativo

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Adicione esta linha para imprimir os erros do formulário
        return super().form_invalid(form)

from django.db.models import Q

class QualitListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Qualit
    template_name = 'listar_qualits.html'
    context_object_name = 'qualits'
    permission_required = 'qualit.view_qualit'  # Substitua 'qualit' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()

        # Recupera os parâmetros da URL
        ID = self.request.GET.get('ID')
        ICCID_NOVO = self.request.GET.get('ICCID_NOVO')
        CLIENTE = self.request.GET.get('CLIENTE')

        # Filtros dinâmicos
        if ID or ICCID_NOVO or CLIENTE:
            filters = Q()
            if ID:
                filters &= Q(ID=ID.strip())
            if ICCID_NOVO:
                filters &= Q(ICCID_NOVO=ICCID_NOVO.strip())
            if CLIENTE:
                filters &= Q(CLIENTE__iexact=CLIENTE.strip())
            
            queryset = queryset.filter(filters)
        else:
            # Retorna todos os registros se nenhum parâmetro for passado
            queryset = queryset.all()

        return queryset

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db import models  # Importando o módulo models do Django
from .models import T42Model
from .forms import T42Form
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class T42ModelListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = T42Model
    template_name = 't42_list.html'
    context_object_name = 'registros'
    paginate_by = 10
    permission_required = 't42.view_t42model'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        estoque_status = self.request.GET.get('estoque_status')

        if search:
            queryset = queryset.filter(
                models.Q(nome__nome__icontains=search) |
                models.Q(id_equipamento__icontains=search)
            )
        if estoque_status:
            queryset = queryset.filter(estoque_status=estoque_status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tets'] = T42Model.objects.filter(equipamento='TETS').count()
        context['total_tets_r'] = T42Model.objects.filter(equipamento='TETS R').count()
        context['total_LOKIES'] = T42Model.objects.filter(equipamento='LOKIES').count()
        context['total_estoque'] = T42Model.objects.filter(estoque_status='Estoque').count()
        context['total_retornando'] = T42Model.objects.filter(estoque_status='Retornando').count()
        context['total_enviado'] = T42Model.objects.filter(estoque_status='enviado').count()
        context['total_extraviado'] = T42Model.objects.filter(estoque_status='extraviado').count()
        context['total_manutencao'] = T42Model.objects.filter(estoque_status='Manutenção').count()
        context['total_registrado'] = T42Model.objects.count()  # Total de todos os equipamentos registrados
        return context

class T42ModelCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = T42Model
    form_class = T42Form
    template_name = 't42_form.html'
    success_url = reverse_lazy('t42_view')
    permission_required = 't42.add_t42model'

    def form_valid(self, form):
        response = super().form_valid(form)
        total_forms = int(self.request.POST.get('total_forms', 0))

        for i in range(total_forms):
            id_equipamento = self.request.POST.get(f'equipamento-{i}-id_equipamento')
            equipamento = self.request.POST.get(f'equipamento-{i}-equipamento')
            status = self.request.POST.get(f'equipamento-{i}-status')
            estoque_status = self.request.POST.get(f'equipamento-{i}-estoque_status')

            if id_equipamento and equipamento and status and estoque_status:
                T42Model.objects.create(
                    nome=self.object.nome,
                    id_equipamento=id_equipamento,
                    equipamento=equipamento,
                    status=status,
                    estoque_status=estoque_status,
                    data=self.object.data
                )

        return response

from django.http import JsonResponse

class UpdateEstoqueStatusView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = T42Model
    fields = ['estoque_status']
    permission_required = 't42.change_t42model'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estoque_status = request.POST.get('estoque_status')
        self.object.save(update_fields=['estoque_status'])

        if request.is_ajax():
            return JsonResponse({'success': True})
        return redirect('t42_view')

class RegistrarEstoqueT42View(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = T42Model
    form_class = T42Form
    template_name = 'registro_estoque_t42.html'
    success_url = reverse_lazy('registrar_estoque_t42')
    permission_required = 't42.add_t42model'
    paginate_by = 10

    def get_queryset(self):
        queryset = T42Model.objects.all()
        search = self.request.GET.get('search')
        estoque_status = self.request.GET.get('estoque_status')

        if search:
            queryset = queryset.filter(
                models.Q(nome__nome__icontains=search) |
                models.Q(id_equipamento__icontains=search)
            )
        if estoque_status:
            queryset = queryset.filter(estoque_status=estoque_status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['t42_estoques'] = self.get_queryset()
        context['total_tets'] = T42Model.objects.filter(equipamento='TETS').count()
        context['total_tets_r'] = T42Model.objects.filter(equipamento='TETS R').count()
        context['total_LOKIES'] = T42Model.objects.filter(equipamento='LOKIES').count()
        context['total_estoque'] = T42Model.objects.filter(estoque_status='Estoque').count()
        context['total_retornando'] = T42Model.objects.filter(estoque_status='Retornando').count()
        context['total_enviado'] = T42Model.objects.filter(estoque_status='enviado').count()
        context['total_extraviado'] = T42Model.objects.filter(estoque_status='extraviado').count()
        context['total_manutencao'] = T42Model.objects.filter(estoque_status='Manutenção').count()
        context['total_registrado'] = T42Model.objects.count()  # Total de todos os equipamentos registrados
        context['search'] = self.request.GET.get('search', '')
        context['estoque_status'] = self.request.GET.get('estoque_status', '')
        return context
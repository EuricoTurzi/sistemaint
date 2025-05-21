from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from .models import Cadastro,Pesquisa
from django.urls import reverse_lazy

class cadastroCreateView(CreateView):
    model = Cadastro
    fields = '__all__'
    template_name = 'cadastro_create.html'
    success_url = reverse_lazy('cadastro_list')
    


class perfilCreateView(CreateView):
    model = Pesquisa
    fields = '__all__'
    template_name = 'pesquisa_create.html'
    success_url = reverse_lazy('pesquisa_list')
    
    
    
class perfilListView(ListView):
    model = Pesquisa
    template_name = 'perfil_list.html'
    context_object_name = 'perfil'
    paginate_by = 10
    
    def get_queryset(self):
        qs = super().get_queryset().order_by('data')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim') 
        empresas = self.request.GET.get('empresa') 
        pesquisa = self.request.GET.get('pesquisa')
        
        if data_inicio and data_fim:
            qs = qs.filter(
                data_entrada__gte=data_inicio,
                data_entrada__lte=data_fim
            ) 
        elif data_inicio:
            qs = qs.filter(data_entrada__gte=data_inicio)
        elif data_fim:
            qs = qs.filter(data_entrada__lte=data_fim)
        if empresas: 
            qs = qs.filter(empresas__icontains = empresas)
        if pesquisa : 
            qs =  qs.filter(pesquisa__icontains = pesquisa)
    
        return qs
    
class cadastroListView(ListView):
    model = Cadastro
    template_name = 'cadastro_list.html'
    context_object_name = 'cadastro'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().order_by('-data_entrada')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        empresas = self.request.GET.get('empresa')
        perfil = self.request.GET.get('perfil')
        plano = self.request.GET.get('plano')
        modo = self.request.GET.get('modo')
        cpf_cnpj = self.request.GET.get('cpf_cnpj')

        if data_inicio and data_fim:
            qs = qs.filter(
                data_entrada__gte=data_inicio,
                data_entrada__lte=data_fim
            ) 
        elif data_inicio:
            qs = qs.filter(data_entrada__gte=data_inicio)
        elif data_fim:
            qs = qs.filter(data_entrada__lte=data_fim)
        
        if empresas:
            qs = qs.filter(empresa__in=empresas.split(',')) 
        if perfil:
            qs = qs.filter(perfil__in=perfil.split(','))
        if plano:
            qs = qs.filter(plano__in=plano.split(','))    
        if modo:
            qs = qs.filter(modo__in=modo.split(','))
        if cpf_cnpj:
            qs = qs.filter(cpf_cnpj__icontains=cpf_cnpj)  # ou use __in se for uma lista exata
	
        return qs
    
    
class perfilUpdateView(UpdateView):
    model= Pesquisa
    fields = '__all__'
    template_name = 'pesquisa_update.html'
    success_url = reverse_lazy('pesquisa_list')


class CadastroUpdateView(UpdateView):
    model= Cadastro
    fields = "__all__"
    template_name = 'cadastro_update.html'
    success_url = reverse_lazy('cadastro_list')

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import ticketmodel
from .forms import ticketForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
class ticketCreateView(LoginRequiredMixin, CreateView):
    model = ticketmodel
    template_name = 'ticket.html'
    form_class = ticketForm
    success_url = reverse_lazy('ticketListView')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Atribui o usuário logado
        return super().form_valid(form)

class ticketListView(ListView):
    model = ticketmodel
    template_name = 'ticket_list.html'
    context_object_name = 'ticket'
    paginate_by = 12

    def get_queryset(self):
        queryset = ticketmodel.objects.all().order_by('-id')
        return queryset

    

def atualizar_status(request, ticket_id):
    ticket = get_object_or_404(ticketmodel, id=ticket_id)
    if ticket.status == 'Pendente':
        ticket.status = 'Atualizado'
        ticket.save()
    return redirect('ticketListView')

def atualizar_status2(request, ticket_id):
    ticket = get_object_or_404(ticketmodel, id=ticket_id)
    if ticket.status == 'Pendente':
        ticket.status = 'Negado'
        ticket.save()
    return redirect('ticketListView')

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import ticketmodel

class DevolutivaUpdateView(UpdateView):
    model = ticketmodel
    template_name = 'atualizar_devolutiva.html'
    fields = ['devolutiva']  # Define o campo que será atualizado
    success_url = reverse_lazy('ticketListView')  # Redireciona após salvar

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Opcional: Atribuir usuário, se necessário
        return super().form_valid(form)
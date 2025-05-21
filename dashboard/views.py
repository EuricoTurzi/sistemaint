from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Lembrete
from .forms import LembreteForm
from django.contrib.auth.mixins import LoginRequiredMixin

class LembretesView(LoginRequiredMixin, CreateView, ListView):
    model = Lembrete
    template_name = 'lembretes.html'
    context_object_name = 'lembretes'
    form_class = LembreteForm
    success_url = reverse_lazy('lembretes')

    def get_queryset(self):
        return Lembrete.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletarLembreteView(LoginRequiredMixin, DeleteView):
    model = Lembrete
    success_url = reverse_lazy('lembretes')

    def get_queryset(self):
        return Lembrete.objects.filter(user=self.request.user)

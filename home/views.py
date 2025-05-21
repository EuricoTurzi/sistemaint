from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role


class HomeView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/home/'  # URL de redirecionamento para a página de login
    permission_required = "home.view_Home"





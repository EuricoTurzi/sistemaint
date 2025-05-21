from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login bem-sucedido
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return render(request, 'register.html', {'register_error': 'Senhas não coincidem'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'register_error': 'Usuário já existe'})
        
        User.objects.create_user(username=username, password=password)
        return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    
    return render(request, 'register.html')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/login/'  # URL de redirecionamento para a página de login

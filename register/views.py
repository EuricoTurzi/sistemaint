from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib.auth.models import User 
from rolepermissions.roles import assign_role 

def login(request): 
    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)

    if user is not None: 
            auth_login(request, user) 
            return redirect('home')
    else: 
        return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
def register(request): 
    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         confirm_password = request.POST.get('confirm_password')
         if password != confirm_password:
              return render(request, 'register.html', {'register_error': 'Senhas não coincidem'})
         if User.objects.filter(username=username).exists():
             return render(request, 'register.html', {'register_error': 'Usuário já existe'})
        
    user = User.objects.create_user(username=username, password=password)
    user.save()
    assign_role(user, 'gerencia')
     # Depuração: Verifique se a função foi atribuída corretamente if user.has_perm('ver') and user.has_perm('editar'): print("Função 'Gerencia' atribuída com sucesso ao usuário.") else: print("Falha ao atribuir a função 'Gerencia' ao usuário.") return redirect('login') return render(request, 'register.html')
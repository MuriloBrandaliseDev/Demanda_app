# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
from django.contrib import messages

def user_login(request):
    """
    View para autenticação de usuários.
    """
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para a home se já estiver logado

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    """
    View para logout de usuários.
    """
    logout(request)
    messages.success(request, "Você foi desconectado com sucesso.")
    return redirect('login')

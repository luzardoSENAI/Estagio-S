from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm   # importa nosso novo form
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

def register_view(request):
    from django.contrib.auth.forms import UserCreationForm
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('lista_livros')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso!')
            return redirect('profile_edit')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'profile_edit.html', {'form': form})

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('lista_livros')  # envia para livros se logado
    return redirect('login')  # envia para login se não logado

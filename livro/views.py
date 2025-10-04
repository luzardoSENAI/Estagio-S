from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm  # Vamos criar um form específico
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

# Novo livro (apenas para usuários logados)
@login_required
def new_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'new_livro.html', {'form': form, 'acao': 'Cadastrar'})


@login_required
def edit_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'new_livro.html', {'form': form, 'acao': 'Alterar'})
# # Reservar um livro
# def reservar_livro(request, livro_id):
#     livro = get_object_or_404(Livro, pk=livro_id)
#     livro.status_livro = 'reservado'
#     livro.save()
#     return redirect('lista_livros')

# # Devolver livro
# def devolver_livro(request, livro_id):
#     livro = get_object_or_404(Livro, pk=livro_id)

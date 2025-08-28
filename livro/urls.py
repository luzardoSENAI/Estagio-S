from django.urls import path
from .views import lista_livros
from . import views

urlpatterns = [
    path('', lista_livros, name='lista_livros'),
    path('new/', views.new_livro, name='new_livro'),    
    path('livros/<int:pk>/editar/', views.edit_livro, name='edit_livro'),# Cadastro de novo livro
]

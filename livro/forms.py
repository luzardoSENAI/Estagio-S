from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['fk_autor', 'fk_editora', 'titulo_livro', 'genero_livro', 'ano_publicacao', 'numero_paginas', 'capa', 'status_livro']

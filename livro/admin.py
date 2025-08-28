from django.contrib import admin
from .models import Autor, Editora, Livro

# Registrando modelos simples
admin.site.register(Autor)
admin.site.register(Editora)

# Registrando Livro com mais opções
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo_livro', 'fk_autor', 'fk_editora', 'ano_publicacao', 'status_livro')
    list_filter = ('status_livro', 'ano_publicacao', 'fk_editora')
    search_fields = ('titulo_livro', 'fk_autor__nome', 'fk_editora__nome')
    ordering = ('titulo_livro',)

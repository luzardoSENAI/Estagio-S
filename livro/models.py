# models.py
import os
from django.db import models
from django.utils.timezone import now
from PIL import Image

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    # outros campos do autor

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    # outros campos da editora

    def __str__(self):
        return self.nome

def caminho_capa(instance, filename):
    """Renomeia o arquivo da capa para evitar conflitos."""
    ext = filename.split('.')[-1]
    nome_arquivo = f"{instance.titulo_livro}_{now().strftime('%Y%m%d%H%M%S')}.{ext}"
    return os.path.join('livro/', nome_arquivo)

class Livro(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
        ('reservado', 'Reservado'),
    ]

    fk_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fk_editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    titulo_livro = models.CharField(max_length=150)
    genero_livro = models.CharField(max_length=50)
    ano_publicacao = models.PositiveSmallIntegerField()
    data_cadastro_livro = models.DateTimeField(auto_now_add=True)
    status_livro = models.CharField(max_length=10, choices=STATUS_CHOICES, default='disponivel')
    numero_paginas = models.PositiveIntegerField()
    capa = models.ImageField(upload_to=caminho_capa, blank=True, null=True)

    def __str__(self):
        return self.titulo_livro

    # def save(self, *args, **kwargs):
    #     """Redimensiona a imagem ao salvar."""
    #     super().save(*args, **kwargs)
    #     if self.capa:
    #         img = Image.open(self.capa.path)
    #         max_size = (300, 300)
    #         img.thumbnail(max_size, Image.ANTIALIAS)
    #         img.save(self.capa.path)





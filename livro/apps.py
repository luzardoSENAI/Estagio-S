from django.apps import AppConfig

class LivroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'livro'  # aqui também deve bater com o nome da pasta do app

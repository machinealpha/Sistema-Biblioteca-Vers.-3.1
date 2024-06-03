from django.apps import AppConfig


class SistemaBibliotecaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sistema_biblioteca_app'

    def ready(self):
        import sistema_biblioteca_app.signals  # Importar las señales

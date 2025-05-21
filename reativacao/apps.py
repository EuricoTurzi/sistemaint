from django.apps import AppConfig


class ReativacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reativacao'
    def ready(self):
        
        import reativacao.signals
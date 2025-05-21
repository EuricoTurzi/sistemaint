from django.apps import AppConfig


class RegistrodemanutencaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registrodemanutencao'

    def ready(self):
        
        import registrodemanutencao.signals

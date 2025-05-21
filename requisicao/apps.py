from django.apps import AppConfig


class RequisicaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'requisicao'
    def ready(self):
        
        import requisicao.signals

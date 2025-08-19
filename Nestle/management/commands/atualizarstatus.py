from django.core.management.base import BaseCommand
from Nestle.models import GridInternacional

class Command(BaseCommand):
    help = 'Atualiza os status existentes no banco de dados para os novos valores padronizados'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando atualização dos status...')
        
        # Conta registros antes da atualização
        total_registros = GridInternacional.objects.count()
        self.stdout.write(f'Total de registros encontrados: {total_registros}')
        
        # Executa a atualização
        GridInternacional.atualizar_status_existentes()
        
        self.stdout.write(self.style.SUCCESS('Atualização dos status concluída com sucesso!')) 

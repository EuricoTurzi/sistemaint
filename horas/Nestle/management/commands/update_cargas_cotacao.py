from django.core.management.base import BaseCommand
from Nestle.models import Carga
import datetime

class Command(BaseCommand):
    help = 'Atualiza as cotações de Dólar e Euro para todas as cargas existentes.'

    def handle(self, *args, **options):
        self.stdout.write("Iniciando a atualização das cotações para cargas existentes...")
        
        cargas_atualizadas = 0
        total_cargas = Carga.objects.count()

        for carga in Carga.objects.all():
            try:
                # Chamar o método save() força a execução da lógica de preenchimento dos campos
                carga.save()
                cargas_atualizadas += 1
                self.stdout.write(f"  Carga ID {carga.id} atualizada. ({cargas_atualizadas}/{total_cargas})")
            except Exception as e:
                self.stderr.write(f"Erro ao atualizar Carga ID {carga.id}: {e}")
        
        self.stdout.write(self.style.SUCCESS(f"Concluída a atualização! {cargas_atualizadas} de {total_cargas} cargas foram atualizadas com sucesso.")) 
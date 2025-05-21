import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Saidas
from produto.models import Produto

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Saidas)
def atualizacao_Produto(sender, instance, created, **kwargs):
    logger.info('atualizacao_Produto foi chamado')
    if created:
        if instance.quantidade > 0:
            produto = Produto.objects.get(id=instance.produto_id)
            produto.refresh_from_db()  # Atualize os dados do produto a partir do banco de dados
            produto.quantidade -= instance.quantidade
            produto.save()
            logger.info(f'A quantidade do produto foi atualizada para {produto.quantidade}')
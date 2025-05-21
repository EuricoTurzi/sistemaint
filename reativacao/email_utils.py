from django.core.mail import EmailMessage
from django.conf import settings

def enviar_email_id_iccid(id_iccid, pdf_path):
    # Configuração do email
    assunto = f'ID ICCID - {id_iccid.id}'
    corpo_email = f'Olá,\n\nSegue em anexo o PDF com as informações do ID ICCID.\n\nAtenciosamente,\nEquipe'
    destinatarios = ['sjuniorr6@gmail.com']  # Ajuste conforme necessário

    # Criação do email
    email = EmailMessage(
        assunto,
        corpo_email,
        settings.DEFAULT_FROM_EMAIL,
        destinatarios,
    )

    # Anexar o PDF
    email.attach_file(pdf_path)

    # Enviar o email
    email.send()
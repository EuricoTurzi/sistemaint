import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.conf import settings
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

def gerar_pdf_id_iccid(id_iccid):
    pdf_path = os.path.join(settings.MEDIA_ROOT, f'id_iccid-{id_iccid.id}.pdf')
    print(f"PDF sendo salvo em: {pdf_path}")  # Adicione isto para depuração
    p = canvas.Canvas(pdf_path, pagesize=letter)
    p.setTitle(f'ID ICCID - {id_iccid.id}')

    # Cabeçalho
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.HexColor("#004B87"))
    y_position = 750
    p.drawString(200, y_position, "ID ICCID")
    y_position -= 30

    # Adicionar imagens de cabeçalho
    imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
    imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
    image_width, image_height = 150, 100
    page_width, page_height = letter
    total_width = image_width * 2 + 20
    x_position = (page_width - total_width) / 2

    # Desenhar as imagens sem o retângulo branco
    p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height, mask='auto')
    p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height, mask='auto')
    y_position -= (image_height + 20)

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    def draw_text(p, theme, value, x, y, max_width):
        theme_style = ParagraphStyle('ThemeStyle', fontName='Helvetica-Bold', fontSize=12)
        value_style = ParagraphStyle('ValueStyle', fontName='Helvetica', fontSize=12)
        
        theme_paragraph = Paragraph(f"<b>{theme}</b>", theme_style)
        value_paragraph = Paragraph(value, value_style)
        
        theme_width, theme_height = theme_paragraph.wrap(max_width, y)
        value_width, value_height = value_paragraph.wrap(max_width, y)
        
        theme_paragraph.drawOn(p, x, y - theme_height)
        y -= theme_height
        value_paragraph.drawOn(p, x, y - value_height)
        y -= value_height + 10  # Espaçamento entre linhas
        
        return y

    def check_space(p, y_position, required_space):
        if y_position - required_space < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 750
        return y_position

    def safe_draw_text(p, theme, value, x, y, max_width):
        if isinstance(value, str):
            return draw_text(p, theme, value, x, y, max_width)
        else:
            return draw_text(p, theme, str(value), x, y, max_width)

    def add_text_with_check(p, theme, value, x, y, max_width):
        required_space = 50  # Espaço necessário para cada entrada de texto
        y = check_space(p, y, required_space)
        return safe_draw_text(p, theme, value, x, y, max_width)

    y_position = add_text_with_check(p, "Reativação:", str(id_iccid.reativacao), 100, y_position, 400)

    # Adicionar todos os id_equipamentos relacionados à mesma reativacao
    for equipamento in id_iccid.reativacao.id_iccids.all():
        y_position = add_text_with_check(p, "ID Equipamento:", equipamento.id_equipamentos, 100, y_position, 400)

    p.showPage()
    p.save()
    print(f"PDF gerado em: {pdf_path}")
    return pdf_path

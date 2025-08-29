from django.shortcuts import render, redirect
from .forms import HorasForm
from .models import horas  # Se o seu modelo for "Horas", ajuste para "from .models import Horas"
import datetime
from dateutil.parser import parse as parse_dt

def parse_datetime_flexible(datetime_str):
    """
    Tenta converter string de data/hora em datetime usando múltiplos formatos.
    Aceita formatos brasileiros e internacionais.
    """
    if not datetime_str or not datetime_str.strip():
        return None
    
    datetime_str = datetime_str.strip()
    
    # Lista de formatos para tentar
    formats = [
        "%Y-%m-%d %H:%M:%S",  # 2024-01-15 14:30:25
        "%Y-%m-%d %H:%M",     # 2024-01-15 14:30
        "%d/%m/%Y %H:%M:%S",  # 15/01/2024 14:30:25
        "%d/%m/%Y %H:%M",     # 15/01/2024 14:30
        "%d/%m/%Y",           # 15/01/2024
        "%Y-%m-%d",           # 2024-01-15
    ]
    
    # Tenta formatos específicos primeiro
    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(datetime_str, fmt)
            # Se o formato não inclui hora, assume 00:00:00
            if fmt in ["%d/%m/%Y", "%Y-%m-%d"]:
                dt = dt.replace(hour=0, minute=0, second=0)
            return dt
        except ValueError:
            continue
    
    # Fallback para dateutil.parser (mais flexível)
    try:
        dt = parse_dt(datetime_str)
        return dt
    except:
        return None

def cadastrar_horas(request):
    if request.method == 'POST':
        form = HorasForm(request.POST, request.FILES)
        if form.is_valid():
            hora_inicial_str = form.cleaned_data.get('hora_inicial')
            hora_final_str = form.cleaned_data.get('hora_final')
            
            # Se 'hora_final' estiver vazia, nula ou for igual a "0", não realiza o cálculo
            if not hora_final_str or hora_final_str.strip() == "" or hora_final_str.strip() == "0":
                formatted_time = "00:00:00"
            else:
                # Usa a função flexível para parsing
                hora_inicial = parse_datetime_flexible(hora_inicial_str)
                hora_final = parse_datetime_flexible(hora_final_str)
                
                if not hora_inicial or not hora_final:
                    form.add_error(None, 'Formato inválido. Use DD/MM/AAAA HH:MM:SS ou AAAA-MM-DD HH:MM:SS para as datas.')
                    return render(request, 'horas.html', {'form': form})
                
                if hora_final <= hora_inicial:
                    form.add_error('hora_final', 'A hora final deve ser maior que a hora inicial.')
                    return render(request, 'horas.html', {'form': form})
                
                diferenca = hora_final - hora_inicial
                total_seconds = int(diferenca.total_seconds())
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = total_seconds % 60
                formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            horas_instance = form.save(commit=False)
            horas_instance.total = formatted_time
            horas_instance.save()
            
            return redirect('consultar_horas')
    else:
        form = HorasForm()
    
    return render(request, 'horas.html', {'form': form})

import datetime
from django.shortcuts import render
from .models import horas  # Se a sua classe for "horas", mantenha; se renomeou para "Horas", ajuste aqui.
import datetime
from django.shortcuts import render
from .models import horas

from django.shortcuts import render
import datetime
from .models import horas

def consulta_horas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final   = request.GET.get('data_final')
    # Inicia queryset e exclui registros aprovados
    qs = horas.objects.all().exclude(status_choice='Aprovado')
    # Filtra por datas se fornecidas
    if data_inicial and data_final:
        qs = qs.filter(
            hora_inicial__gte=data_inicial,
            hora_final__lte=data_final
        )

    employee_data = []
    grand_seconds = 0

    # percorre cada funcionário distinto
    for func_id in qs.values_list('funcionario', flat=True).distinct():
        records = qs.filter(funcionario=func_id)
        total_seconds = 0

        # soma os intervalos somente dos não-aprovados
        for item in records:
            hi = parse_datetime_flexible(item.hora_inicial)
            hf = parse_datetime_flexible(item.hora_final)
            if hi and hf and hf > hi:
                total_seconds += int((hf - hi).total_seconds())

        grand_seconds += total_seconds

        # formata para HH:MM:SS
        h, resto = divmod(total_seconds, 3600)
        m, s     = divmod(resto, 60)
        formatted = f"{h:02d}:{m:02d}:{s:02d}"

        # atualiza total_de_horas no banco (opcional)
        records.update(total_de_horas=formatted)

        employee_data.append({
            'funcionario': records.first().funcionario if records.exists() else '',
            'records':     records,
            'total':       formatted,
        })

    # total geral
    h, resto = divmod(grand_seconds, 3600)
    m, s     = divmod(resto, 60)
    grand_total = f"{h:02d}:{m:02d}:{s:02d}"

    return render(request, 'tabela_horas.html', {
        'employee_data': employee_data,
        'grand_total':   grand_total,
        'data_inicial':  data_inicial,
        'data_final':    data_final,
    })


from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import horas   # ou se o modelo foi renomeado para "Horas", ajuste aqui
from .forms import HorasForm

class HorasUpdateView(UpdateView):
    model = horas
    form_class = HorasForm
    template_name = "update_horas.html"
    success_url = reverse_lazy('consultar_horas')  # Altere para a URL de sucesso desejada

    


# views.py
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import horas

@require_POST
def aprovar_horas(request, pk):
    obj = get_object_or_404(horas, pk=pk)
    obj.status_choice = 'Aprovado'
    obj.save()
    return JsonResponse({'status': obj.status_choice})
from io import BytesIO
import datetime
from dateutil.parser import parse as parse_dt
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from .models import horas

def safe_parse(dt_str, pk):
    """
    Tenta converter `dt_str` em datetime.
    Emite DEBUG no console.
    """
    if not dt_str or not dt_str.strip():
        print(f"[DEBUG][{pk}] string vazia para parse")
        return None
    s = dt_str.strip()
    # 1) tente formatos rígidos
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            dt = datetime.datetime.strptime(s, fmt)
            print(f"[DEBUG][{pk}] parse '{s}' com strptime({fmt}) → {dt}")
            return dt
        except ValueError:
            # ignora
            pass
    # 2) fallback dateutil
    try:
        dt = parse_dt(s)
        print(f"[DEBUG][{pk}] parse '{s}' com dateutil → {dt}")
        return dt
    except Exception as e:
        print(f"[DEBUG][{pk}] falha dateutil.parse('{s}') → {e}")
        return None



from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
import os
import datetime
from io import BytesIO
from dateutil.parser import parse as parse_dt
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from django.conf import settings
from .models import horas

def consulta_horas_pdf(request):
    # Captura parâmetros de data (se houver)
    data_ini = request.GET.get('data_inicial')
    data_fin = request.GET.get('data_final')

    # Inicia queryset excluindo registros já aprovados
    qs = horas.objects.exclude(status_choice='Aprovado')
    if data_ini and data_fin:
        qs = qs.filter(hora_inicial__gte=data_ini, hora_final__lte=data_fin)

    # Usa a função flexível de parsing já definida
    # (parse_datetime_flexible já está disponível globalmente)

    # Agrupa dados por funcionário
    employee_data = []
    for func_id in qs.values_list('funcionario', flat=True).distinct():
        records = qs.filter(funcionario=func_id)
        total_seconds = 0
        rows = []
        for it in records:
            hi = parse_datetime_flexible(it.hora_inicial)
            hf = parse_datetime_flexible(it.hora_final)
            diff = (hf - hi).total_seconds() if hi and hf and hf > hi else 0
            total_seconds += int(diff)
            h, rem = divmod(int(diff), 3600)
            m, s = divmod(rem, 60)
            row_total = f"{h:02d}:{m:02d}:{s:02d}"
            # Formatar datas para DD/MM/AAAA
            hi_str = hi.strftime("%d/%m/%Y") if hi else ""
            hf_str = hf.strftime("%d/%m/%Y") if hf else ""
            rows.append({
                'hora_inicial': hi_str,
                'hora_final':   hf_str,
                'motivo':       it.motivo or "",
                'total':        row_total,
            })
        # Total agregado por funcionário
        h, rem = divmod(total_seconds, 3600)
        m, s = divmod(rem, 60)
        agg_total = f"{h:02d}:{m:02d}:{s:02d}"
        employee_data.append({
            'funcionario': records.first().funcionario,
            'rows':        rows,
            'agg_total':   agg_total,
        })

    # Monta documento
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    wrap_style = ParagraphStyle('wrap', parent=styles['Normal'], fontSize=8, leading=10)
    bold_style = ParagraphStyle('bold', parent=styles['Normal'], fontSize=8, leading=10, fontName='Helvetica-Bold')

    story = []
    story.append(Spacer(1, 12))

    title = Paragraph(
        "Relatório de Horas<br/>Dep de Inteligência e Desenvolvimento",
        ParagraphStyle(name='CenterTitle', parent=styles['Title'], alignment=1, spaceAfter=12)
    )
    story.append(title)

    if data_ini and data_fin:
        story.append(Paragraph(f"Período: {data_ini} a {data_fin}", styles['Normal']))
        story.append(Spacer(1, 6))

    # Gera tabelas por funcionário, apenas registros pendentes
    for emp in employee_data:
        story.append(Paragraph(f"Funcionário: {emp['funcionario']}", styles['Heading3']))
        data = [[
            Paragraph("Hora Inicial", wrap_style),
            Paragraph("Hora Final", wrap_style),
            Paragraph("Motivo", wrap_style),
            Paragraph("Total", wrap_style),
        ]]
        for row in emp['rows']:
            data.append([
                Paragraph(row['hora_inicial'], wrap_style),
                Paragraph(row['hora_final'], wrap_style),
                Paragraph(row['motivo'], wrap_style),
                Paragraph(row['total'], wrap_style),
            ])
        data.append([
            "", "",
            Paragraph("Total de Horas:", bold_style),
            Paragraph(emp['agg_total'], bold_style),
        ])
        tbl = Table(data, colWidths=[4*cm, 4*cm, 7*cm, 3*cm])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('ALIGN', (3,-1), (3,-1), 'RIGHT'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('FONTNAME', (2,-1), (3,-1), 'Helvetica-Bold'),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 24))

    doc.build(story)
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')






import datetime
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.views.decorators.http import require_GET
from django.conf import settings

# Importe sua função que gera o PDF
from .views import consulta_horas_pdf

@require_GET
def enviar_email_relatorio_horas(request):
    """
    Envia por e‑mail o PDF gerado por consulta_horas_pdf em anexo.
    Em caso de falha, redireciona de volta para a página de consulta.
    """
    try:
        print("=== INICIANDO ENVIO DE EMAIL ===")
        
        # Gera o PDF
        print("1. Gerando PDF...")
        pdf_response = consulta_horas_pdf(request)
        pdf_content = pdf_response.content
        print(f"   PDF gerado com {len(pdf_content)} bytes")

        # Assunto e corpo
        hoje = datetime.datetime.now().strftime("%d/%m/%Y")
        subject = f"Relatório de Horas - {hoje} Departamento de Inteligência"
        body = f"""Olá,

Segue em anexo o relatório de horas do período solicitado.

Data de geração: {hoje}

Atenciosamente,
Sistema de Gestão de Horas"""

        # Destinatários
        recipients = [
            'julio.cesar@grupogoldensat.com.br',
            'rh@grupogoldensat.com.br',
            'sjuniorr6@gmail.com',
        ]

        print("2. Preparando email...")
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=recipients
        )

        # Anexa o PDF
        filename = f'relatorio_horas_{hoje}.pdf'
        email.attach(filename, pdf_content, 'application/pdf')
        print(f"   PDF anexado: {filename}")

        # Envia
        print("3. Enviando email...")
        email.send(fail_silently=False)
        print("   ✅ Email enviado com sucesso!")
        
        # Adiciona mensagem de sucesso
        from django.contrib import messages
        messages.success(request, 'Relatório enviado por email com sucesso!')

    except Exception as e:
        # Log do erro para debug
        print(f"❌ ERRO AO ENVIAR EMAIL: {str(e)}")
        print(f"   Tipo do erro: {type(e).__name__}")
        import traceback
        print(f"   Traceback completo:")
        traceback.print_exc()
        
        # Adiciona mensagem de erro
        from django.contrib import messages
        messages.error(request, f'Erro ao enviar email: {str(e)}')

    # Retorna para consulta_horas
    return redirect('consultar_horas')




from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import horas

@require_POST
def validar_hora(request):
    pk = request.POST.get('pk')
    hora = get_object_or_404(horas, pk=pk)
    hora.status_choice = 'Aprovado'
    hora.save(update_fields=['status_choice'])
    return JsonResponse({'status':'success'})







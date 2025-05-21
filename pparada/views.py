from django.shortcuts import render
from django.urls import reverse_lazy
from .models import paradasegura, passagemmodel
from .forms import paradaForm, PassagemModelForm
from django.views.generic import CreateView, ListView, DetailView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont
import os

class paradaCreateView(CreateView):
    model = paradasegura
    template_name = 'parada_create.html'
    form_class = paradaForm
    success_url = reverse_lazy('paradaseguraform')

    def form_valid(self, form):
        # Salva o objeto primeiro
        response = super().form_valid(form)

        # Lista dos campos de imagem a serem verificados para aplicar a marca d'água
        campos_imagem = ['foto_cavalo', 'foto_documento_cavalo', 'foto_carreta', 'foto_carreta_documento', 'cnh']

        # Itera sobre os campos de imagem e aplica a marca d'água se a imagem existir
        for campo in campos_imagem:
            imagem = getattr(self.object, campo, None)
            if imagem and hasattr(imagem, 'path') and os.path.exists(imagem.path):
                print(f"Aplicando marca d'água na imagem: {imagem.path}")
                add_watermark(imagem.path)

        return response

def add_watermark(image_path, watermark_text="Grupo Golden Sat / Parada Segura"):
    try:
        if not os.path.exists(image_path):
            print(f"Imagem não encontrada: {image_path}")
            return

        original_image = Image.open(image_path).convert("RGBA")
        print(f"Imagem original carregada com sucesso: {image_path}")

        txt_layer = Image.new("RGBA", original_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        try:
            font = ImageFont.truetype("arial.ttf", 48)
        except IOError:
            font = ImageFont.load_default()

        text_width, text_height = draw.textsize(watermark_text, font=font)
        padding = 20
        text_position = (original_image.width - text_width - padding, original_image.height - text_height - padding)

        draw.text(text_position, watermark_text, fill=(255, 255, 255, 255), font=font)
        print(f"Marca d'água adicionada na posição: {text_position}")

        watermarked_image = Image.alpha_composite(original_image, txt_layer)
        watermarked_image = watermarked_image.convert("RGB")
        watermarked_image.save(image_path, format="JPEG")
        print(f"Marca d'água aplicada com sucesso em {image_path}")

    except Exception as e:
        print(f"Erro ao aplicar marca d'água: {e}")

class passagemCreateView(CreateView):
    model = passagemmodel
    template_name = 'passagem.html'
    form_class = PassagemModelForm
    success_url = reverse_lazy('passagemCreateView')

class PassagemListView(ListView):
    model = passagemmodel
    template_name = 'historico_passagem.html'
    context_object_name = 'passagens'
    paginate_by = 10

    def get_queryset(self):
        return passagemmodel.objects.all().order_by('-data_criacao')

class historicoListView(ListView):
    model = paradasegura
    template_name = 'historico_paradas.html'
    context_object_name = 'pa'
    paginate_by = 10

    def get_queryset(self):
        queryset = paradasegura.objects.all().order_by('-data_criacao')
        embarcador = self.request.GET.get('embarcador')
        if embarcador:
            queryset = queryset.filter(embarcador__icontains=embarcador)
        return queryset

class Parada2DetailView(DetailView):
    model = paradasegura
    template_name = 'parada_detail2.html'
    context_object_name = 'parada'

class paradaListView(ListView):
    model = paradasegura
    template_name = 'pa_list.html'
    context_object_name = 'pa'
    paginate_by = 12

    def get_queryset(self):
        queryset = paradasegura.objects.filter(status='AGUARDANDO').order_by('-id')
        embarcador = self.request.GET.get('embarcador', None)
        if embarcador:
            queryset = queryset.filter(Q(embarcador__icontains=embarcador))
        return queryset

class RegistrarSaidaView(View):
    def get(self, request, pk, *args, **kwargs):
        parada = get_object_or_404(paradasegura, pk=pk)
        parada.status = 'EM VIAGEM'
        parada.saida = timezone.now()
        parada.save()
        return redirect('paradaseguralist')

class ParadaDetailView(DetailView):
    model = paradasegura
    template_name = 'parada_detail.html'
    context_object_name = 'parada'

def get_choices(request):
    tipo_posto = request.GET.get('tipo_posto')
    print(f'Tipo de posto: {tipo_posto}')
    response_data = {
        'iscas': [],
        'cadeados': [],
        'pa': []
    }

    if tipo_posto:
        if tipo_posto in paradasegura.POSTOS_INFO1:
            iscas = paradasegura.POSTOS_INFO1[tipo_posto].get('iscas', [])
            cadeados = paradasegura.POSTOS_INFO1[tipo_posto].get('cadeados', [])
            response_data['iscas'] = iscas
            response_data['cadeados'] = cadeados
            print(f'Iscas: {iscas}, Cadeados: {cadeados}')

        if tipo_posto in paradasegura.POSTOS_INFO2:
            pa = paradasegura.POSTOS_INFO2[tipo_posto].get('pa', [])
            response_data['pa'] = pa
            print(f'PA: {pa}')
    return JsonResponse(response_data)

def get_pa_choices(request):
    tipo_posto = request.GET.get('tipo_posto')
    print(f'Tipo de posto: {tipo_posto}')
    if tipo_posto and tipo_posto in passagemmodel.POSTOS_INFO2:
        pa = passagemmodel.POSTOS_INFO2[tipo_posto]['pa']
        print(f'PA: {pa}')
        return JsonResponse({'pa': pa})
    return JsonResponse({'pa': []})

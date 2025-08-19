from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import GridInternacional
from .serializers import GridInternacionalUpdateSerializer

class GridInternacionalUpdateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_planilha):
        objetos = GridInternacional.objects.filter(id_planilha=id_planilha)

        if not objetos.exists():
            return Response({'error': 'Registro não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = GridInternacionalUpdateSerializer(objetos, many=True)
        return Response(serializer.data)

    def put(self, request, id_planilha):
        objetos = GridInternacional.objects.filter(id_planilha=id_planilha)

        if not objetos.exists():
            # Criação caso não exista nenhum
            data = request.data.copy()
            data['id_planilha'] = id_planilha
            serializer = GridInternacionalUpdateSerializer(data=data)
            if serializer.is_valid():
                equipamento = serializer.save()
                return Response({
                    'success': True,
                    'created': True,
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Atualiza todos os encontrados
        erros = []
        atualizados = []
        for obj in objetos:
            serializer = GridInternacionalUpdateSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                equipamento = serializer.save()
                atualizados.append(GridInternacionalUpdateSerializer(equipamento).data)
            else:
                erros.append(serializer.errors)

        if erros:
            return Response({'partial_success': True, 'errors': erros}, status=status.HTTP_207_MULTI_STATUS)

        return Response({
            'success': True,
            'updated_count': len(atualizados),
            'data': atualizados
        }, status=status.HTTP_200_OK)

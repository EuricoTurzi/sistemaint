from rest_framework import serializers
from .models import GridInternacional

class GridInternacionalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GridInternacional
        fields = [ 'bl', 'container', 'destino']

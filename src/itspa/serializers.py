from rest_framework import serializers

from .models import Proceso, Archivo

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Archivo
        fields ='__all__'
class ProcesoSerializer(serializers.ModelSerializer):
    archivo_proceso = ArchivoSerializer(many=True, read_only=True)
    class Meta:
        model = Proceso
        fields= '__all__'
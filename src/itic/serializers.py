from rest_framework import serializers
from .models import Teacher
from .models import Proceso
from .models import Archivo
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields= '__all__'
class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Archivo
        fields ='__all__'
class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields= '__all__'

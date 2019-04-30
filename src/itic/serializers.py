from rest_framework import serializers
from .models import Teacher,Nivel,Formacion_Academica
 
class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'
class FormacionAcademicaSerializer(serializers.ModelSerializer):
    nivel = NivelSerializer(many=False, read_only=True)
    class Meta:
        model = Formacion_Academica
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    formacion = FormacionAcademicaSerializer(many=True,read_only=True)
    class Meta:
        model = Teacher
        fields= '__all__'

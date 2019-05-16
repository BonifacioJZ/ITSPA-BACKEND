from rest_framework import serializers
from .models import Teacher,Nivel,Formacion_Academica, New, Tag
from django.contrib.auth.models import User
 
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id','username'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields ='__all__'

class NewSerializer(serializers.ModelSerializer):
    usuario  = UserSerializer(many=False,read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = New
        fields ='__all__'               

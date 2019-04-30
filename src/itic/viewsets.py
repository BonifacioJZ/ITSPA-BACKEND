from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

#Modelos
from .models import Formacion_Academica, New, Nivel, Teacher
from .serializers import (FormacionAcademicaSerializer, NewSerializer,
                          NivelSerializer, TeacherSerializer,UserSerializer)


class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class FormacionAcademicaViewSet(viewsets.ModelViewSet):
    queryset = Formacion_Academica.objects.all()
    serializer_class = FormacionAcademicaSerializer
class TeacherViewSet(viewsets.ModelViewSet):
    queryset= Teacher.objects.all()
    serializer_class= TeacherSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class= NewSerializer

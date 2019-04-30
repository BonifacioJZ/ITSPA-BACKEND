from rest_framework import viewsets
#Modelos
from .models import Teacher, Nivel, Formacion_Academica
from .serializers import TeacherSerializer,NivelSerializer,FormacionAcademicaSerializer

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class FormacionAcademicaViewSet(viewsets.ModelViewSet):
    queryset = Formacion_Academica.objects.all()
    serializer_class = FormacionAcademicaSerializer
class TeacherViewSet(viewsets.ModelViewSet):
    queryset= Teacher.objects.all()
    serializer_class= TeacherSerializer

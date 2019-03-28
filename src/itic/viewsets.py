from rest_framework import viewsets
#Modelos
from .models import Teacher
from .models import Proceso
from .models import Archivo
#Serializers
from .serializers import TeacherSerializer
from .serializers import ProcesoSerializer
from .serializers import ArchivoSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset= Teacher.objects.all()
    serializer_class= TeacherSerializer
class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
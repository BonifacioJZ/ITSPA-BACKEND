from rest_framework import viewsets


from .models import Archivo, Proceso
from .serializers import ArchivoSerializer, ProcesoSerializer


class ProcesoViewSet(viewsets.ModelViewSet):
    queryset= Proceso.objects.all()
    serializer_class= ProcesoSerializer
class ArchivoViewSet(viewsets.ModelViewSet):
    queryset= Archivo.objects.all()
    serializer_class= ArchivoSerializer

from rest_framework import viewsets
#Modelos
from .models import Teacher

#Serializers
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset= Teacher.objects.all()
    serializer_class= TeacherSerializer

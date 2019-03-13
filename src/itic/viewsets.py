from rest_framework import viewsets
from .models import teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset= teacher.objects.all()
    serializer_class= TeacherSerializer

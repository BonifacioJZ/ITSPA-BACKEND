from rest_framework import routers
from .viewsets import TeacherViewSet
from .viewsets import ProcesoViewSet
from .viewsets import ArchivoViewSet

router = routers.SimpleRouter()
router.register('teachers',TeacherViewSet)
router.register('procesos',ProcesoViewSet)
router.register('archivos',ArchivoViewSet)

urlpatterns = router.urls
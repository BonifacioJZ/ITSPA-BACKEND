from rest_framework import routers
from .viewsets import ArchivoViewSet,ProcesoViewSet


router = routers.SimpleRouter()
router.register('archivos',ArchivoViewSet)
router.register('procesos',ProcesoViewSet)
urlpatterns = router.urls
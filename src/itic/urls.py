from rest_framework import routers
from .viewsets import TeacherViewSet,NivelViewSet,FormacionAcademicaViewSet


router = routers.SimpleRouter()
router.register('teachers',TeacherViewSet)
router.register('niveles',NivelViewSet)
router.register('formacion',FormacionAcademicaViewSet)

urlpatterns = router.urls
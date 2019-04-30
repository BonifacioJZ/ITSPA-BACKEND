from rest_framework import routers
from .viewsets import TeacherViewSet,NivelViewSet,FormacionAcademicaViewSet,NewViewSet,UserViewSet


router = routers.SimpleRouter()
router.register('usuarios',UserViewSet)
router.register('teachers',TeacherViewSet)
router.register('niveles',NivelViewSet)
router.register('formacion',FormacionAcademicaViewSet)
router.register('noticias',NewViewSet)

urlpatterns = router.urls
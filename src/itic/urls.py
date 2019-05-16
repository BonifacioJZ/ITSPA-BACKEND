from rest_framework import routers
from .viewsets import (TeacherViewSet,NivelViewSet,FormacionAcademicaViewSet,
NewViewSet,UserViewSet,TagViewSet)


router = routers.SimpleRouter()
router.register('usuarios',UserViewSet)
router.register('teachers',TeacherViewSet)
router.register('niveles',NivelViewSet)
router.register('formacion',FormacionAcademicaViewSet)
router.register('noticias',NewViewSet)
router.register('tags',TagViewSet)

urlpatterns = router.urls
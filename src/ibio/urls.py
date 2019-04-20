from rest_framework import routers
from .viewsets import TeacherViewSet


router = routers.SimpleRouter()
router.register('teachers',TeacherViewSet)

urlpatterns = router.urls
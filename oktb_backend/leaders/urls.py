from django.urls import path
from rest_framework import routers

from .views import LeaderViewSet

router = routers.DefaultRouter()
router.register('', LeaderViewSet)

urlpatterns = router.urls
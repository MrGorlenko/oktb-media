from django.urls import path
from rest_framework import routers

from .views import NewsViewSet

router = routers.DefaultRouter()
router.register('', NewsViewSet)

urlpatterns = router.urls
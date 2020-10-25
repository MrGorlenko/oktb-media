from django.urls import path
from rest_framework import routers

from .views import ArticleViewSet

router = routers.DefaultRouter()
router.register('', ArticleViewSet)

urlpatterns = router.urls
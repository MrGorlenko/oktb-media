from django.urls import path
from rest_framework import routers

from .views import LeaderViewSet, LeaderCategoryViewSet

router = routers.DefaultRouter()
router.register('leaders', LeaderViewSet, basename='leaders')
router.register('leaders_categories', LeaderCategoryViewSet, basename='leaders_category')

urlpatterns = router.urls
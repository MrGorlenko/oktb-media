from django.urls import path
from rest_framework import routers

from .views import ArticleViewSet, ThemeViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('themes', ThemeViewSet, basename='themes')

urlpatterns = router.urls

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article, Theme
from .serializers import ArticlesSerializer, ThemeSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer


class ThemeViewSet(ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticlesSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

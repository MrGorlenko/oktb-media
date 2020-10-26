from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import News
from .serializers import NewsSerializer


class ArticleViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
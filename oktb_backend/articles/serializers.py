from rest_framework import serializers
from .models import Article, Theme


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'theme', 'title', 'date', 'content', 'img', 'is_active', 'hot')


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'name', 'is_active')

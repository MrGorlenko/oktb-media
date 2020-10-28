from rest_framework import serializers
from .models import Article, Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'name', 'is_active')


class ArticlesSerializer(serializers.ModelSerializer):

    theme = serializers.CharField(source='theme.name', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'theme', 'title', 'date', 'content', 'img', 'is_active', 'hot')




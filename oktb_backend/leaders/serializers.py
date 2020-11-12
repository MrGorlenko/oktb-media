from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Leader, LeaderCategory


class LeaderCategorySerializer(ModelSerializer):
    class Meta:
        model = LeaderCategory
        fields = ['id', 'title', 'label', 'active']


class LeaderSerializer(ModelSerializer):

    category = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Leader
        fields = ['id', 'name', 'category', 'link', 'img', 'audience', 'job', 'phone', 'mail', 'top']




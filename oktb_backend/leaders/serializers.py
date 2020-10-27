from rest_framework.serializers import ModelSerializer
from .models import Leader, LeaderCategory


class LeaderSerializer(ModelSerializer):
    class Meta:
        model = Leader
        fields = ['id', 'name', 'link', 'img', 'audience']


class LeaderCategorySerializer(ModelSerializer):
    class Meta:
        model = LeaderCategory
        fields = ['id', 'title', 'label', 'active']

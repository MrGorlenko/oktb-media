from rest_framework.serializers import ModelSerializer
from .models import Leader, LeaderCategory


class LeaderSerializer(ModelSerializer):
    class Meta:
        model = Leader
        fields = ['id', 'name', 'category', 'link', 'img', 'audience', 'job', 'phone', 'mail', 'top']


class LeaderCategorySerializer(ModelSerializer):
    class Meta:
        model = LeaderCategory
        fields = ['id', 'title', 'label', 'active']

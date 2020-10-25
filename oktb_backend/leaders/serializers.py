from rest_framework.serializers import ModelSerializer
from .models import Leader


class LeaderSerializer(ModelSerializer):
    class Meta:
        model = Leader
        fields = ['id', 'name', 'link', 'img', 'audience']

from rest_framework.serializers import ModelSerializer
from .models import Video


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'date', 'img', 'about', 'video']

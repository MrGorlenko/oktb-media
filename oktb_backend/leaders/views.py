from rest_framework.viewsets import ModelViewSet
from .serializers import LeaderSerializer
from .models import Leader


class LeaderViewSet(ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer

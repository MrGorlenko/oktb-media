from rest_framework.viewsets import ModelViewSet
from .serializers import LeaderSerializer, LeaderCategorySerializer
from .models import Leader, LeaderCategory


class LeaderViewSet(ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer


class LeaderCategoryViewSet(ModelViewSet):
    queryset = LeaderCategory.objects.all()
    serializer_class = LeaderCategorySerializer


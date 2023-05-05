# Create your views here.
from rest_framework import viewsets
from nursbook.tags.models import Tag
from nursbook.tags.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
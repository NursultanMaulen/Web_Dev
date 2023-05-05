# serializers.py
from rest_framework import serializers
from nursbook.tags.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')



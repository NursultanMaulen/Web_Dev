from django.db import models
#from django.contrib.auth.models import User
from nursbook.users.models import User
from nursbook.tags.models import Tag
from rest_framework import serializers
from nursbook.articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    favorited = serializers.SerializerMethodField()
    favoritesCount = serializers.SerializerMethodField()
    tagList = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())

    class Meta:
        model = Article
        fields = ('title', 'description', 'body', 'tagList', 'created_at', 'updated_at', 'favorited', 'favoritesCount', 'author', 'slug')
        read_only_fields = ('created_at', 'updated_at', 'favorited', 'favoritesCount', 'author', 'slug')

    def create(self, validated_data):
        tagList = validated_data.pop('tagList')
        print(validated_data)
        article = Article.objects.create(**validated_data)
        article.tagList.set(tagList)
        article.save()
        return article

    def update(self, instance, validated_data):
        if 'tagList' in validated_data:
            tagList = validated_data.pop('tagList')
            instance.tagList.set(tagList)
        return super().update(instance, validated_data)

    def get_favorited(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return True
        return False

    def get_favoritesCount(self, obj):
        return 1000

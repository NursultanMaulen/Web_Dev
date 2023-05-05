from django.db import models
from django.contrib.auth.models import User
from nursbook.tags.models import Tag
# Create your models here.

class Article(models.Model):
    slug = models.CharField(max_length=255, default="DEFAULT SLUG")
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tagList = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

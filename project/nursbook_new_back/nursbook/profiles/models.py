from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=300, blank=True)
    image = models.URLField(blank=True)
    # following = models.ManyToManyField('self', symmetrical=False, related_name='followed_by')

    def __str__(self):
        return self.user.username

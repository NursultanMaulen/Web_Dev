from rest_framework import serializers
from nursbook.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    bio = serializers.CharField(required=False)
    image = serializers.URLField(required=False)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image')

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

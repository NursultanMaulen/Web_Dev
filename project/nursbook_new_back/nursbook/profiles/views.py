from django.shortcuts import render

# Create your views here.

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nursbook.profiles.models import Profile
from nursbook.profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'

    @action(detail=True, methods=['post'])
    def follow(self, request, user__username=None):
        user_profile = self.get_object()
        follower_profile = request.user.profile
        if user_profile == follower_profile:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        user_profile.followed_by.add(follower_profile)
        user_profile.save()
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def unfollow(self, request, user__username=None):
        user_profile = self.get_object()
        follower_profile = request.user.profile
        user_profile.followed_by.remove(follower_profile)
        user_profile.save()
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset

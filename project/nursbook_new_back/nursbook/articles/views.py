from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from nursbook.articles.models import Article
from nursbook.articles.serializers import ArticleSerializer


class ArticleViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    A viewset for the articles endpoint that supports the following actions:
        - GET /api/articles/ (list articles)
        - GET /api/articles/feed/ (list articles by followed users)
        - GET /api/articles/:slug/ (retrieve a single article)
        - POST /api/articles/ (create a new article)
        - PUT /api/articles/:slug/ (update an existing article)
        - DELETE /api/articles/:slug/ (delete an existing article)
        - POST /api/articles/:slug/favorite/ (favorite an article)
        - DELETE /api/articles/:slug/favorite/ (unfavorite an article)
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)

    @action(detail=True, methods=['POST'])
    def favorite(self, request, slug=None):
        article = self.get_object()
        user = request.user.profile
        user.favorite(article)
        serializer = self.get_serializer(article)
        return Response(serializer.data)

    @favorite.mapping.delete
    def unfavorite(self, request, slug=None):
        article = self.get_object()
        user = request.user.profile
        user.unfavorite(article)
        serializer = self.get_serializer(article)
        return Response(serializer.data)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


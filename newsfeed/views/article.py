from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from newsfeed.models.article import Article
from newsfeed.pagination import ArticlePagination
from newsfeed.serializers.article import (
    GetFavoritesArticleSerializer,
    ResponseArticleSerializer,
    RequestCreateArticleSerializer
)
from user.serializers.user import UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ResponseArticleSerializer
    queryset = Article.objects.all()
    pagination_class = ArticlePagination
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """Choose serializer for input data."""
        if self.action == "create":
            return RequestCreateArticleSerializer
        if self.action == "list":
            return ResponseArticleSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()

        default_ordering = ['-rating', '-created_at']
        queryset = queryset.order_by(*default_ordering)

        return queryset


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Инкрементируем счетчик просмотров
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddFavoriteArticlesView(GenericViewSet, ViewSet):
    serializer_class = ResponseArticleSerializer
    queryset = Article.objects.all()

    @action(detail=True, methods=['POST'])
    def add_to_favorites(self, request, pk=None):
        article = self.get_object()
        user = request.user
        article.favorites.add(user)
        article.save()
        return Response({'message': 'Article added to favorites'})


class RemoveFromFavoritesArticlesView(GenericViewSet, ViewSet):
    serializer_class = ResponseArticleSerializer
    queryset = Article.objects.all()

    @action(detail=True, methods=['POST'])
    def remove_from_favorites(self, request, pk=None):
        article = self.get_object()
        user = request.user
        article.favorites.remove(user)
        article.save()
        return Response({'message': 'Article removed from favorites'})


class GetFavoritesArticlesView(GenericViewSet, ViewSet):
    serializer_class = ResponseArticleSerializer
    queryset = Article.objects.all()

    @action(detail=True, methods=['GET'])
    def favorited_by(self, request, pk=None):
        article = self.get_object()
        favorited_users = article.favorites.all()
        serializer = UserSerializer(favorited_users, many=True)
        return Response(serializer.data)


class GetUserFavoritesArticlesView(GenericViewSet, ViewSet):
    serializer_class = ResponseArticleSerializer
    queryset = Article.objects.all()

    @action(detail=False, methods=['GET'])
    def favorites(self, request):
        user = request.user  # Получаем текущего пользователя
        favorited_articles = Article.objects.filter(favorites=user)
        serializer = GetFavoritesArticleSerializer(favorited_articles, many=True)
        return Response(serializer.data)

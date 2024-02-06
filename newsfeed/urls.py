from django.urls import path, include
from rest_framework.routers import SimpleRouter


from newsfeed.views.article import (
    ArticleViewSet,
    AddFavoriteArticlesView,
    RemoveFromFavoritesArticlesView,
    GetFavoritesArticlesView,
    GetUserFavoritesArticlesView,
)

article_router = SimpleRouter()
article_router.register(
    prefix="article", viewset=ArticleViewSet, basename="article"
)
article_router.register(
    prefix="article", viewset=AddFavoriteArticlesView, basename="add-favorite"
)
article_router.register(
    prefix="article", viewset=RemoveFromFavoritesArticlesView, basename="remove-favorite"
)
article_router.register(
    prefix="article", viewset=GetFavoritesArticlesView, basename="get-favorites-by-article"
)
article_router.register(
    prefix="article", viewset=GetUserFavoritesArticlesView, basename="get-favorites-articles-by-user"
)


urlpatterns = [
    path('', include(article_router.urls)),
]

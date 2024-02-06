from rest_framework import serializers

from newsfeed.models.article import Article


class ResponseArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'created_at',
                  'author', 'views', 'favorites', 'assessment', 'rating']

        def update(self, instance, validated_data):
            # Увеличиваем счетчик просмотров на 1
            instance.views += 1
            instance.save()
            return instance


class RequestCreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content']

        def update(self, instance, validated_data):
            # Увеличиваем счетчик просмотров на 1
            instance.views += 1
            instance.save()
            return instance


class GetFavoritesArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'views', 'rating', 'assessment']


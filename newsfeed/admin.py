from django.contrib import admin
from newsfeed.models.article import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title_in_transliteration', 'title', 'author', 'summary',
                    'views', 'assessment', 'rating')



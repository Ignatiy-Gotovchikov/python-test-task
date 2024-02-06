from django.db import models
from transliterate import translit
from django.utils.text import slugify


from newsfeed.constants import ASSESSMENT_CHOICES
from user.models import User


class Article(models.Model):
    article = models.AutoField(verbose_name='Article number', primary_key=True)

    title_in_transliteration = models.CharField(
        max_length=255, verbose_name='Title in transliteration', null=True, blank=True
    )

    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name="Article text")
    created_at = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_articles')
    summary = models.CharField(max_length=250, verbose_name='Summary')
    views = models.PositiveIntegerField(verbose_name='Number of views', default=0)
    favorites = models.ManyToManyField(User, related_name='favorite_articles', blank=True)
    assessment = models.CharField(max_length=255, choices=ASSESSMENT_CHOICES, default=0, verbose_name='Assessment')
    rating = models.PositiveIntegerField(verbose_name='Rating', default=0)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def save(self, *args, **kwargs):
        self.title_in_transliteration = translit(self.title, 'ru', reversed=True)
        self.slug = slugify(self.title_in_transliteration)
        super().save(*args, **kwargs)


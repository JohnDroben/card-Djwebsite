from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import Truncator


class NewsPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    excerpt = models.CharField("Краткое описание", max_length=300, blank=True)
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_date = models.DateTimeField('Дата обновления', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

    def get_short_excerpt(self):
        if self.excerpt:
            return self.excerpt
        return Truncator(self.content).chars(150, truncate='...')

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-pub_date']
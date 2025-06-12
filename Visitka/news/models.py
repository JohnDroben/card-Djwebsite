from django.db import models
from django.contrib.auth.models import User




class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    content = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    post_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    is_published = models.BooleanField('Опубликована', default=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']


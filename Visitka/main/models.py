from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True,
        verbose_name='Фото профиля'
    )
    bio = models.TextField('О себе', blank=True)
    skills = models.TextField('Навыки', blank=True)
    experience = models.TextField('Опыт работы', blank=True)
    is_public = models.BooleanField('Публичный профиль', default=True)

    def __str__(self):
        return f"Профиль {self.user.username}"
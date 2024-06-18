from django.contrib.auth.models import AbstractUser
from django.db import models
from habitApp.constants import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE, help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE, help_text='Загрузите фото')
    country = models.CharField(max_length=20, verbose_name='Страна', **NULLABLE, help_text='Введите страну')
    city = models.CharField(max_length=20, verbose_name='Город', **NULLABLE, help_text='Введите город')
    chat_id = models.CharField(max_length=100, verbose_name='ID чата', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

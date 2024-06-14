from django.db import models

from app import settings
from habitApp.constants import NULLABLE, DAYS


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='related_owner',
        verbose_name='Владелец привычки'
    )
    place = models.CharField(
        max_length=100,
        verbose_name='Место действия',
        help_text='Укажите место выполнение действия'
    )
    at_action = models.DateTimeField(
        verbose_name='Время действия',
        help_text='укажите в какое время выполнять действие'
    )
    action = models.CharField(
        max_length=50,
        verbose_name='Действие',
        help_text='укажите действие')
    is_nice_habit = models.BooleanField(
        default=False,
        verbose_name='Признак приятной привычки',
        help_text='отметьте привычку если она относится к приятным привычкам'
    )
    associated_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='related_habits',
        verbose_name='Связанная привычка',
        help_text='укажите ID приятной привычки'
    )
    periodicity = models.CharField(
        max_length=15,
        choices=DAYS,
        default='daily',
        verbose_name='Периодичность действия',
        help_text='выберете периодичность'
    )
    reward = models.CharField(
        max_length=100,
        verbose_name='Вознаграждение',
        help_text='укажите вознаграждение'
    )
    time_to_complete = models.TimeField(
        verbose_name='Время на выполнение действия',
        help_text='укажите сколько понадобится времени на выполнение действия (максимальное время 2 минуты)'
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name='Признак публичности',
        help_text='отметьте если хотите сделать привычку публичной'
    )

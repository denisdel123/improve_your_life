import os
from celery import shared_task
from django.db.models import Q
from django.utils import timezone
from habitApp.models import Habit
from habitApp.services import send_message

"""Задача celery для напоминания по телеграмм о запланированных привычках."""


@shared_task
def send_notification():  # Функция отправки уведомления
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    today = timezone.now().weekday()
    time_now = timezone.now().time()
    habits = Habit.objects.filter(Q(periodicity=weekdays[today]) | Q(periodicity='daily'))
    token = os.getenv('TELEGRAM_TOKEN_BOT')

    for habit in habits:

        if habit.at_action >= time_now:
            message = f"Не забудь про привычку '{habit.action}'\n" \
                      f"После этого можно:\n \
{habit.associated_habit if habit.associated_habit else habit.reward}"

            if habit.owner.chat_id:
                send_message(
                    token=token,
                    chat_id=habit.owner.chat_id,
                    message=message
                )

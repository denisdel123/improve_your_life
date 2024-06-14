from datetime import time

from rest_framework import serializers
from habitApp.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ['owner']

    def validate(self, data):
        is_nice_habit = data.get('is_nice_habit')
        associated_habit = data.get('associated_habit')
        reward = data.get('reward')

        if is_nice_habit and (associated_habit or reward):
            raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связной привычки")

        if 'associated_habit' in data and 'reward' in data:

            if data['associated_habit'] is not None and data['reward'] is not None:
                raise serializers.ValidationError(
                    "Вы не можете выбрать вознаграждение и связную привычку одновременно")

        return data

    def validate_time_to_complete(self, value):
        max_time = time(minute=2)
        if value > max_time:
            raise serializers.ValidationError("время на выполнение не должно превышать 120 секунд или 2 минуты")
        return value

    def validate_associated_habit(self, value):
        if value and not value.is_nice_habit:
            raise serializers.ValidationError("Только приятные привычки могут быть связными")
        return value





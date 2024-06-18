from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from UserApp.models import User
from habitApp.models import Habit


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        """Заполнение БД"""
        self.user = User.objects.create(email="test1@mail.ru")
        self.user1 = User.objects.create(email="test2@mail.ru")
        self.client.force_authenticate(self.user)

        self.habit_nice = Habit.objects.create(
            owner=self.user,
            place="Москва",
            action="выпить стакан воды",
            is_nice_habit=True,
            time_to_complete="00:01:30"
        )
        self.habit_reward = Habit.objects.create(
            owner=self.user,
            place="Москва",
            action="выпить стакан воды",
            reward='Плавание',
            time_to_complete="00:01:30"
        )
        self.habit = Habit.objects.create(
            owner=self.user1,
            place="Москва",
            action="Завтрак",
            reward='Час игр',
            time_to_complete="00:2:00",
            is_public=True

        )

    def test_create_habit(self):
        """Тестирования создания привычки."""
        data = {
            "place": "Москва",
            "action": "выпить стакан воды",
            "is_nice_habit": True,
            "time_to_complete": "00:01:30"

        }
        url = reverse('habitApp:habit-create')

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json()["place"], data['place']
        )

        """Тестирование валидации приятной привычки и вознаграждения."""
        data = {
            "place": "Москва",
            "action": "выпить стакан воды",
            "is_nice_habit": True,
            "time_to_complete": "00:01:30",
            "reward": "Прогулка в парке",

        }
        response = self.client.post(url, data)

        self.assertIn(
            "У приятной привычки не может быть вознаграждения или связной привычки",
            response.content.decode()
        )

        """Тестирование валидации приятной привычки и связной привычки."""
        data = {
            "place": "Москва",
            "action": "выпить стакан воды",
            "is_nice_habit": True,
            "time_to_complete": "00:01:30",
            "associated_habit": 1

        }
        response = self.client.post(url, data)
        self.assertIn(
            "У приятной привычки не может быть вознаграждения или связной привычки",
            response.content.decode()
        )

        """Тестирование валидации выбора вознаграждения и связной привычки одновременно."""
        data = {
            "place": "Москва",
            "action": "выпить стакан воды",
            "time_to_complete": "00:01:30",
            "reward": "Прогулка в парке",
            "associated_habit": 1

        }
        response = self.client.post(url, data)

        self.assertIn(
            "Вы не можете выбрать вознаграждение и связную привычку одновременно",
            response.content.decode()
        )

        """Тестирование валидации выбора времени выше условного."""
        data = {
            "place": "Москва",
            "action": "выпить стакан воды",
            "time_to_complete": "00:02:30",
            "reward": "Прогулка в парке",
            "associated_habit": 1

        }
        response = self.client.post(url, data)

        self.assertIn(
            "время на выполнение не должно превышать 120 секунд или 2 минуты",
            response.content.decode()
        )

        """Тестирование валидации выбора привычки без признака приятной."""
        data = {
            "place": "Москва",
            "action": "выпить стакан воды",
            "time_to_complete": "00:02:00",
            "reward": "Прогулка в парке",
            "associated_habit": 2

        }
        response = self.client.post(url, data)

        self.assertIn(
            "Только приятные привычки могут быть связными",
            response.content.decode()
        )

    def test_list_habit(self):
        url = reverse("habitApp:habit-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()['results']),
            2
        )

    def test_list_public_habit(self):
        url = reverse("habitApp:habit-list-public")
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()["results"]), 1
        )

    def test_update_habit(self):
        url = reverse("habitApp:habit-update", args=(self.habit_nice.pk,))
        data = {
            "place": "Джакарта"
        }

        response = self.client.patch(url, data, format="json")
        print(response.json)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()["place"], "Джакарта"
        )

    def test_destroy_habit(self):
        url = reverse("habitApp:habit-destroy", args=(self.habit_nice.pk,))

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Habit.objects.all().count(), 2
        )

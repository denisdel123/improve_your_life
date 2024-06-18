from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from UserApp.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test1@mail.ru')

    def test_register_user(self):
        """Тестирования регистрации пользователя."""

        url = reverse('usersApp:user-create')
        data = {
            'email': 'test2@mail.ru',
            'password1': 'Qwer123456',
            'password2': 'Qwer123456'
        }

        response = self.client.post(
            url,
            data,
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        url = reverse('usersApp:user-create')
        data = {
            'email': 'test3@mail.ru',
            'password1': 'Qwer123456',
            'password2': 'Wwer123456'
        }

        response = self.client.post(
            url,
            data,
        )

        # Проверяем, что запрос вернул код статуса 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Проверяем, что в ответе присутствует сообщение об ошибке валидации пароля
        self.assertIn("Пароль не совпадает!", response.content.decode())

        url = reverse('usersApp:user-create')
        data = {
            'email': 'test2@mail.ru',
            'password1': 'Qwer123456',
            'password2': 'Qwer123456'
        }

        response = self.client.post(
            url,
            data,
        )

        # Проверяем, что запрос вернул код статуса 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Проверяем, что в ответе присутствует сообщение об ошибке валидации пароля
        self.assertIn('Пользователь with this Почта already exists.', response.content.decode())

    def test_list_user(self):
        url = reverse('usersApp:user-list')
        self.client.force_authenticate(self.user)

        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        self.assertEqual(
            len(response.data), 1
        )

    def test_retrieve_user(self):
        self.client.force_authenticate(self.user)
        url = reverse(
            'usersApp:user-retrieve',
            args=(self.user.pk,)
        )

        response = self.client.get(url)
        data = response.json()
        now = self.user.date_joined
        str_now = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        result = {'id': self.user.pk,
                  'password': self.user.password,
                  'last_login': self.user.last_login,
                  'is_superuser': self.user.is_superuser,
                  'first_name': self.user.first_name,
                  'last_name': self.user.last_name,
                  'is_staff': self.user.is_staff,
                  'is_active': self.user.is_active,
                  'date_joined': str_now,
                  'email': self.user.email,
                  'phone': self.user.phone,
                  'avatar': None,
                  'country': self.user.country,
                  'city': self.user.city,
                  'chat_id': self.user.chat_id,
                  'groups': [],
                  'user_permissions': []
                  }

        self.assertEqual(
            data['email'], self.user.email,
        )

        self.assertEqual(
            data, result
        )

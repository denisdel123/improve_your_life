from rest_framework.test import APITestCase

from UserApp.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user1 = User.objects.create(email='test1@mail.ru', is_superuser=True)
        self.user2 = User.objects.create(email='test2@mail.ru')
        self.client.force_authenticate(self.user1)

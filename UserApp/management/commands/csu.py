import os

from django.core.management import BaseCommand

from UserApp.models import User
from app.settings import EMAIL_SUPERUSER_ENV, PASSWORD_SUPERUSER_ENV


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=EMAIL_SUPERUSER_ENV,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password(PASSWORD_SUPERUSER_ENV)

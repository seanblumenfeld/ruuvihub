import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist."

    def handle(self, *args, **options):
        username = os.getenv('INITIAL_ADMIN_USER')
        password = os.getenv('INITIAL_ADMIN_PASSWORD')
        if not username or not password:
            raise ValueError('Expected INITIAL_ADMIN_USER and INITIAL_ADMIN_PASSWORD '
                             'environment variables to be set.')

        model = get_user_model()
        if not model.objects.filter(username=username).exists():
            model.objects.create_superuser(username=username, password=password)

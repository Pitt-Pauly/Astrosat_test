from django.conf import settings
from django.core.management.base import BaseCommand
import os

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

Usere = get_user_model()

class Command(BaseCommand):
    help = "Creates a dummy super user account based on provided .env variables, see code for details."

    def handle(self, *args, **options):
        username = os.environ['DUMMY_USERNAME']
        email = os.environ['DUMMY_EMAIL']
        password = os.environ['DUMMY_PASSWORD']
        self.stdout.write('Creating account for %s (%s)' % (username, email))
        try:
            admin = User.objects.get(username=username)
            self.stdout.write('Dummy Admin account exists already!')
        except User.DoesNotExist:
            admin = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                is_active=True,
            )
            self.stdout.write('Default Admin account was successfully created!')
from django.conf import settings
from django.core.management.base import BaseCommand
import os

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

Usere = get_user_model()

class Command(BaseCommand):
    help = "Creates a dummy super user account based on provided arguments, else it creates a default admin account."

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            action='store',
            default='admin',
            help='username of dummy admin, if none provided will attempt to read env variable DUMMY_USERNAME'
        )
        parser.add_argument(
            '--email',
            action='store',
            default='admin@mysite.com',
            help='email of dummy admin, if none provided will attempt to read env variable DUMMY_EMAIL'
        )
        parser.add_argument(
            '--password',
            action='store',
            default='supersafe111',
            help='password of dummy admin, if none provided will attempt to read env variable DUMMY_PASSWORD'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
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
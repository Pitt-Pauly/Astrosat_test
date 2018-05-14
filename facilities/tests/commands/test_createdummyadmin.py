import os
from io import StringIO

from django.contrib.auth import get_user_model
from django.db.models.base import ObjectDoesNotExist
from django.core.management import call_command
from django.test import TestCase
from django.conf import settings
from facilities.models import Facility

User = get_user_model()

class CreateDummyAdminTest(TestCase):

    def setUp(self):
        self.dummy = {
            'username': 'admin',
            'email': 'admin@mysite.com',
            'password': 'supersafe22'
        }

    def test_command_default(self):
        try:
            user = User.objects.get(
                username=self.dummy['username'],
                email=self.dummy['email']
            )
        except User.DoesNotExist:
            user = None

        self.assertIsNone(user)

        out = StringIO()
        call_command('createdummyadmin', stdout=out, **self.dummy)
        self.assertIn('Default Admin account was successfully created!', out.getvalue())

        try:
            user = User.objects.get(
                username=self.dummy['username'],
                email=self.dummy['email']
            )
        except User.DoesNotExist:
            user = None

        self.assertIsNotNone(user)


    def test_command_rerun(self):
        out = StringIO()
        call_command('createdummyadmin', stdout=out, **self.dummy)
        self.assertIn('Default Admin account was successfully created!', out.getvalue())

        try:
            user = User.objects.get(
                username=self.dummy['username'],
                email=self.dummy['email']
            )
        except User.DoesNotExist:
            user = None

        self.assertIsNotNone(user)

        out = StringIO()
        call_command('createdummyadmin', stdout=out, **self.dummy)
        self.assertIn('Dummy Admin account exists already!', out.getvalue())
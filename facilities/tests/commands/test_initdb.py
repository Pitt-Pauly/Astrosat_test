import os
from io import StringIO

from django.db.models.base import ObjectDoesNotExist
from django.core.management import call_command
from django.test import TestCase
from django.conf import settings
from facilities.models import Facility

class InitdbTest(TestCase):
    def test_command_output_default(self):
        out = StringIO()
        filepath = settings.INIT_DB_DEFAULT_JSON
        call_command('initdb', stdout=out)
        self.assertIn('Loading JSON data from file %s into database' % filepath, out.getvalue())
        self.assertIn('Successfully initialized Database with JSON', out.getvalue())

        Facility.objects.get(center="Stennis Space Center", facility="Test Stand A-2 #4122")
        Facility.objects.get(center="Goddard Space Flight Center", facility="500 WSC: Antenna, 10m S-band")

    def test_command_output_test_json(self):
        out = StringIO()
        filepath = os.path.abspath('facilities/tests/commands/data/test.json')
        call_command('initdb', filepath, stdout=out)
        self.assertIn('Loading JSON data from file %s into database' % filepath, out.getvalue())
        self.assertIn('Successfully initialized Database with JSON', out.getvalue())

        Facility.objects.get(center="AstroSat HQ", facility="Test Stand A-1 #1337")
        Facility.objects.get(center="Astro Space Center", facility="Test Stand A-2 #1338")

class InitdbAddTest(TestCase):
    def test_adding_more_facilitites(self):
        # first load the NASA dataset
        out = StringIO()
        filepath = settings.INIT_DB_DEFAULT_JSON
        call_command('initdb', stdout=out)
        self.assertIn('Loading JSON data from file %s into database' % filepath, out.getvalue())
        self.assertIn('Successfully initialized Database with JSON', out.getvalue())

        # then add to it two facilities
        filepath = os.path.abspath('facilities/tests/commands/data/test.json')
        call_command('initdb', filepath, stdout=out)
        self.assertIn('Loading JSON data from file %s into database' % filepath, out.getvalue())
        self.assertIn('Successfully initialized Database with JSON', out.getvalue())

        Facility.objects.get(center="Stennis Space Center", facility="Test Stand A-2 #4122")
        Facility.objects.get(center="Goddard Space Flight Center",
                             facility="500 WSC: Antenna, 10m S-band")
        Facility.objects.get(center="AstroSat HQ", facility="Test Stand A-1 #1337")
        Facility.objects.get(center="Astro Space Center", facility="Test Stand A-2 #1338")
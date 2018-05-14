import argparse

from django.conf import settings
from django.core.management.base import BaseCommand
from rest_framework.utils import json
from facilities.serializers import FacilitySerializer

from facilities.models import Facility

class Command(BaseCommand):
    help = 'Initializes the default database with the data parsed from the given JSON file.'

    def add_arguments(self, parser):
        default_file = settings.BASE_DIR + '/facilities/fixtures/9g7e-7hzz.json'

        parser.add_argument(
            'filepath',
            default=default_file,
            help='Path to file containing JSON payload from NASA\'s Facilities API Endpoint'
        )

    def handle(self, *args, **options):
        # go through json and for each object in list, validate data via serializer, and save object.
        filepath = options['filepath']
        with open(filepath) as f:
            data = json.load(f)
            serializer = FacilitySerializer(data=data, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                self.stdout.write(self.style.SUCCESS('Successfully initialized Database with JSON in file "%s"' % filepath))
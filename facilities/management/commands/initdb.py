import argparse

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from rest_framework.utils import json
from facilities.serializers import FacilitySerializer

from facilities.models import Facility

class Command(BaseCommand):

    try:
        default_file = settings.INIT_DB_DEFAULT_JSON
    except AttributeError:
        raise CommandError('Please assign a value to INIT_DB_DEFAULT_JSON in the settings before continuing.')

    help = 'Initializes the default database with the data parsed from the given JSON file.' \
           'default file to be used: "%s" ' % default_file

    def add_arguments(self, parser):
        parser.add_argument(
            dest='filepath',
            action='store',
            nargs='?',
            default=self.default_file,
            help='Path to file containing JSON payload from NASA\'s Facilities API Endpoint, will use default if none given'
        )

    def handle(self, *args, **options):
        # go through json and for each object in list, validate data via serializer, and save object.
        filepath = self.default_file
        if options['filepath']:
            filepath = options['filepath']

        if filepath is None or filepath == '':
            raise CommandError(
                'No filepath given and default filepath could not be retrieved from the settings. '
                'is INIT_DB_DEFAULT_JSON set?'
            )

        self.stdout.write(self.style.NOTICE('Loading JSON data from file %s into database...' % filepath))

        with open(filepath) as f:
            data = json.load(f)
            serializer = FacilitySerializer(data=data, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                self.stdout.write(self.style.SUCCESS('Successfully initialized Database with JSON'))
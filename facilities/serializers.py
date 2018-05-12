from rest_framework import serializers
from .models import Facility

class FacilitySerializer(serializers.ModelSerializer):
    # def validate(self, data):
    #     try:
    #         location_data = {
    #             'coordinates': data.pop('location'),
    #             'state': data.pop('state', None),
    #             'country': data.pop('country', None),
    #             'zip': data.pop('location_zip', None),
    #             'address': data.get('facility', None)
    #         }
    #     except KeyError as ke:
    #         raise serializers.ValidationError('Location coordinates are required to specify a location, but none found.')
    #
    #     loc_serializer = LocationSerializer(data=location_data)
    #     loc_serializer.is_valid(raise_exception=True)

    class Meta():
        model = Facility
        fields = ( 'center',
                   'center_search_status',
                   'facility',
                   'facility_url',
                   'occupied',
                   'status',
                   'url_link',
                   'record_date',
                   'last_update',
                   'location',
                   'city',
                   'state',
                   'country',
                   'zipcode',
                )
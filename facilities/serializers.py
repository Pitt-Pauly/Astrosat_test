from collections import OrderedDict

from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Facility, Location

# class PointFieldSerializer(serializers.Field):
#
#     def to_representation(self, instance: PointField):
#         return [ float(instance.lon), float(instance.lat) ]
#
#     def to_internal_value(self, data):
#         if isinstance(data, list):
#             lon, lat = [ float(i) for i in data ]
#             ret = OrderedDict( { 'lon': lon, 'lat': lat } )
#         else:
#             ret = super(PointFieldSerializer, self).to_internal_value(data)
#         return ret
#
#     class Meta():
#         model = PointField
#         fields = ("lon", "lat")

class LocationSerializer(serializers.ModelSerializer):
    coordinates = serializers.ListField(
        child=serializers.FloatField()
    )

    def get_coordinates(self):
        return [ self.lon, self.lat ]

    def to_representation(self, instance: Location):
        return [ float(instance.lon), float(instance.lat) ]

    class Meta():
        model = Location
        fields = ("type", "coordinates")

class FacilitySerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create_from_coordinates(**location_data)
        facility = Facility.objects.create(location=location,**validated_data)
        return facility

    def update(self, instance, validated_data):
        """
        If the location data is not set, we don't want to change anything.
        If new location data is provided, the location record is updated, this is ok since for each facility
        there is just one location
        """
        location_data = validated_data.pop('location', None)
        if location_data is not None:
            location = instance.location
            location.type = location_data.get('type', location.type )
            coords = location_data.get('coordinates')
            if coords is not None:
                location.lon = coords[0]
                location.lat = coords[1]
            location.save()

        instance.center = validated_data.get('center', instance.center)
        instance.center_search_status = validated_data.get('center_search_status', instance.center_search_status)
        instance.facility = validated_data.get('facility', instance.facility)
        instance.facility_url = validated_data.get('facility_url', instance.facility_url)
        instance.occupied = validated_data.get('occupied', instance.occupied)
        instance.status = validated_data.get('status', instance.status)
        instance.url_link = validated_data.get('url_link', instance.url_link)
        instance.record_date = validated_data.get('record_date', instance.record_date)
        instance.last_update = validated_data.get('last_update', instance.last_update)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)

        instance.save()

        return instance

    class Meta():
        model = Facility
        fields = (
            'id',
            'center',
            'center_search_status',
            'facility',
            'facility_url',
            'occupied',
            'status',
            'url_link',
            'record_date',
            'last_update',
            'contact',
            'phone',
            'location',
            'city',
            'state',
            'country',
            'zipcode',
        )
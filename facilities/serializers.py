from collections import OrderedDict

from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Facility, Location, PointField

class PointFieldSerializer(serializers.Field):

    def to_representation(self, instance: PointField):
        return [ float(instance.lon), float(instance.lat) ]

    def to_internal_value(self, data):
        if isinstance(data, list):
            lon, lat = [ float(i) for i in data ]
            ret = OrderedDict( { 'lon': lon, 'lat': lat } )
        else:
            ret = super(PointFieldSerializer, self).to_internal_value(data)
        return ret

    class Meta():
        model = PointField
        fields = ("lon", "lat")

class LocationSerializer(serializers.ModelSerializer):
    coordinates = PointFieldSerializer()

    class Meta():
        model = Location
        fields = ("type", "coordinates")

class FacilitySerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        coords = location_data.pop('coordinates')
        point = PointField.objects.create(**coords)
        location = Location.objects.create(coordinates=point, **location_data)
        facility = Facility.objects.create(location=location,**validated_data)
        return facility

    def update(self, instance, validated_data):
        # I am assuming that if the location data is not set, we don't want to change anything
        location_data = validated_data.pop('location', default=None)
        if location_data is not None:
            coords = location_data.pop('coordinates', default=None)
            if coords is not None:
                point = instance.location.coordinates
                point.lon = coords[0]
                point.lat = coords[1]
                point.save()
            location = instance.location
            location.type = location_data.get('type', location.type )
            location.coordinates = location_data.get('coordinates', location.coordinates)
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
from django.contrib.gis.db import models

class Location(models.Model):
    coordinates = models.PointField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    zip = models.CharField(primary_key=True)

class Facility(models.Model):
    center = models.CharField()
    center_search_status = models.CharField(
        choices=("Public", "Private")
    )
    facility = models.CharField()
    facility_url = models.URLField()
    occupied = models.DateTimeField()
    status = models.CharField(
        choices=('Active', 'Inactive')
    )
    url_link = models.URLField()
    record_date = models.DateTimeField()
    last_update = models.DateTimeField()
    contact = models.CharField()
    phone = models.CharField()
    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE,

    )
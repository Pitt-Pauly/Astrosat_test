from django.contrib.gis.db import models

class Facility(models.Model):
    center = models.CharField(required=True, blank=False, null=False)
    center_search_status = models.CharField(
        choices=("Public", "Private"),
        required=True
    )
    facility = models.CharField(required=True, blank=False, null=False)
    facility_url = models.URLField(required=False, blank=False, null=True)
    occupied = models.DateTimeField(required=True, blank=False, null=False)
    status = models.CharField(
        choices=('Active', 'Inactive'),
        required=True,
        blank=False,
        null=False,
    )
    url_link = models.URLField(required=False, blank=False, null=True)
    record_date = models.DateTimeField(required=True, blank=False, null=False)
    last_update = models.DateTimeField(required=True, blank=False, null=False)
    contact = models.CharField(required=False, blank=False, null=True)
    phone = models.CharField(required=False, blank=False, null=True)

    location = models.PointField(required=True, blank=False, null=False)
    # address = models.CharField(blank=False, null=True)
    city = models.CharField(blank=False, null=True)
    state = models.CharField(blank=False, null=True)
    country = models.CharField(blank=False, null=True)
    zipcode = models.CharField(blank=False, null=True)
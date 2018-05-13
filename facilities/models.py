from django.db import models
from django.utils.translation import ugettext_lazy as _

class PointFieldManager(models.Manager):

    def create_from_coordinates(self, coords):
        data = {
            'lon': coords[0],
            'lat': coords[1],
        }
        point = self.create(data)
        return point


class PointField(models.Model):
    lat = models.FloatField(
        unique=False,
        blank=False,
        null=False
    )
    lon = models.FloatField(
        unique=False,
        blank=False,
        null=False
    )

    objects = PointFieldManager()

    class Meta():
        verbose_name = _('point')
        verbose_name_plural = _('points')

class LocationManager(models.Manager):

    def create_with_Point_using_coordinates(self, validated_data):
        coords = validated_data.get('coordinates', default=None)
        point = PointField.objects.create(**coords)
        location = Location.objects.create(coordinates=point, **validated_data)
        return location

class Location(models.Model):
    type = models.CharField(
        max_length=10,
        choices=(
            ("Point" , _("Point")),
        ),
        default="Point"
    )
    coordinates = models.ForeignKey(
        to=PointField,
        on_delete=models.CASCADE
    )

    objects = LocationManager()

    class Meta():
        verbose_name = _('location')
        verbose_name_plural = _('locations')

class Facility(models.Model):
    center = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    center_search_status = models.CharField(
        max_length=10,
        choices=(
            ("Public", _("Public")),
            ("Private", _("Private"))
        ),
        blank=False,
        null=False
    )
    facility = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )
    status = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        default="Inactive"
    )

    facility_url = models.URLField( blank=True, null=False )
    url_link = models.URLField( blank=True, null=False )

    occupied = models.DateTimeField( blank=True, null=False )
    record_date = models.DateTimeField(blank=False, null=False)
    last_update = models.DateTimeField(blank=True, null=False)

    contact = models.CharField(
        max_length=150,
        blank=True,
        null=False
    )
    phone = models.CharField(
        max_length=25,
        blank=True,
        null=False
    )

    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE
    )

    city = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    state = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    country = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    zipcode = models.CharField(
        max_length=15,
        blank=False,
        null=False
    )

    class Meta():
        verbose_name = _('facility')
        verbose_name_plural = _('facilities')
        unique_together = (('center', 'facility'),)
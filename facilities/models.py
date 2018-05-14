from django.db import models
from django.utils.translation import ugettext_lazy as _

class LocationManager(models.Manager):

    def create_from_coordinates(self, coordinates: list, type="Point"):
        data = {
            'type': type,
            'lon': coordinates[0],
            'lat': coordinates[1],
        }
        location = self.create(**data)
        return location

class Location(models.Model):
    type = models.CharField(
        max_length=10,
        choices=(
            ("Point" , _("Point")),
        ),
        default="Point"
    )

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

    facility_url = models.URLField( blank=True, null=True )
    url_link = models.URLField( blank=True, null=True )

    occupied = models.DateTimeField( blank=True, null=True )
    record_date = models.DateTimeField( blank=False, null=True )
    last_update = models.DateTimeField( blank=True, null=True )

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
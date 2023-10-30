from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

DISTRICT_CHOICES = [
    ('Northern District', 'Northern District'),
    ('Eastern District', 'Eastern District'),
    ('Western District', 'Western District'),
    ('Southern District', 'Southern District'),
    ('Wellington City', 'Wellington City'),
]

LEVEL_CHOICES = [
    ('weak', 'weak'),
    ('Moderate', 'Moderate'),
    ('Strong', 'Strong'),
    ('Severe', 'Severe'),
]

class Earthquake(models.Model):
    name = models.CharField(_('City '), max_length=100, unique=True)
    district = models.CharField(
        _('District'), max_length=30, choices=DISTRICT_CHOICES)
    region = models.CharField(_('region'), max_length=50)
    level = models.CharField(
        _('Seisimic Intensity'), max_length=30, choices=LEVEL_CHOICES)
    location = models.PointField(_('location'), srid=2193)
    created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Date Updated'), auto_now=False)

    def __str__(self):
        return self.name

    def get_school_first_name(self):
        return self.name.split()[0]
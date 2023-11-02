from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

DISTRICT_CHOICES = [
    ('Northern district', 'Northern district'),
    ('Eastern district', 'Eastern district'),
    ('Western district', 'Western district'),
    ('Southern district', 'Southern district'),
    ('Wellington City', 'Wellington City'),

]

LEVEL_CHOICES = [
    ('Weak', 'Weak'),
    ('Light', 'Light'),
    ('Moderate', 'Moderate'),
    ('Strong', 'Strong'),
    ('Severe', 'Severe'),
    ('Extreme', 'Extreme'),

]

class earthquake(models.Model):
    city = models.CharField(_('City'), max_length=100, unique=True)
    district = models.CharField(
        _('District'), max_length=30, choices=DISTRICT_CHOICES)
    shaking = models.CharField(
        _('Shaking'), max_length=30, choices=LEVEL_CHOICES)
    location = models.PointField(_('Location'), srid=2193)
    created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Date Updated'), auto_now=False)

    def __str__(self):
        return self.name
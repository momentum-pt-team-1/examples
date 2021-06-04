from django.db import models
from django.contrib.auth.models import User

from localflavor.us.models import USPostalCodeField


class Profile(models.Model):
    PIEDMONT = 'PM'
    MOUNTAINS = 'MT'
    COASTAL_PLAIN = 'CP'

    REGION_CHOICES = [
        (PIEDMONT, 'Piedmont'),
        (MOUNTAINS, 'Mountains'),
        (COASTAL_PLAIN, 'Coastal Plain'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = USPostalCodeField()
    experience_level = models.IntegerField()
    moniker = models.CharField(max_length=240)
    effort_level = models.IntegerField()
    region = models.CharField(choices=REGION_CHOICES, max_length=100)

    def __str__(self):
        return self.moniker


class Plant(models.Model):
    common_name = models.CharField(max_length=240, blank=True, null=True)
    scientific_name = models.CharField(max_length=240, blank=True, null=True)
    zones = models.ManyToManyField('GrowingZone', related_name="plants")

    def __str__(self):
        return self.common_name if self.common_name else self.scientific_name


class GrowingZone(models.Model):
    A = 'A'
    B = 'B'
    
    ZONE_CHOICES = [
        (A, 'a'),
        (B, 'b')
    ]
    number = models.IntegerField()
    subdivision = models.CharField(max_length=1, choices=ZONE_CHOICES)

# python script for making growing Zones in US
# for i in range(14):
# ...     for sub in ['A', 'B']:
# ...             GrowingZone.objects.create(number=i, subdivision=sub)
    
    def __str__(self):
        return f'{self.number} {self.subdivision}'

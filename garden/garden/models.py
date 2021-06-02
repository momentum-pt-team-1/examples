from django.db import models
from django.contrib.auth.models import User

from localflavor.us.models import USPostalCodeField





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = USPostalCodeField()
    experience_level = models.IntegerField()
    moniker = models.CharField(max_length=240)
    effort_level = models.IntegerField()

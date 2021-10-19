from django.db import models
from django.conf import settings


class UserModel(models.Model):
    ip = models.CharField(max_length=30, blank=True, null=True)
    continent_name = models.CharField(max_length=20, blank=True, null=True)
    country_name = models.CharField(max_length=40, blank=True, null=True)
    region_name = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)
    longitude = models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)
  # datetime = models.DateField(max_length=50, blank=True, null=True)

   # class Meta:
   #     ordering = ['-datetime']

    def __str__(self):
        return self.ip
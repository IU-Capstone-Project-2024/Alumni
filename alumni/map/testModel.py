from django.db import models
from geopy.geocoders import Nominatim

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.city and self.country and not (self.latitude and self.longitude):
            geolocator = Nominatim(user_agent="alumni_site")
            location_str = f"{self.city}, {self.country}"
            location = geolocator.geocode(location_str)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super().save(*args, **kwargs)

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from geopy.geocoders import Nominatim

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     user_photo = models.ImageField(upload_to='profile_pics/', blank=True)
#     graduation_year = models.IntegerField(null=True, blank=True)
#     position = models.CharField(max_length=50, blank=True)
#     company = models.CharField(max_length=50, blank=True)
#     city = models.CharField(max_length=50, blank=True)
#     country = models.CharField(max_length=50, blank=True)
#     interests = models.TextField(blank=True, null=True)
#     activities = models.TextField(blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     tg_alias = models.CharField(max_length=50, blank=True)
#     latitude = models.FloatField(null=True, blank=True)
#     longitude = models.FloatField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if self.city and self.country:
#             geolocator = Nominatim(user_agent="alumni_site")
#             location = geolocator.geocode(f"{self.city}, {self.country}")
#             if location:
#                 self.latitude = location.latitude
#                 self.longitude = location.longitude
#         super().save(*args, **kwargs)
# In map/models.py (assuming this is where CustomUser is defined)

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from geopy.geocoders import Nominatim

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    user_photo = models.ImageField(upload_to='profile_pics/', blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    interests = models.TextField(blank=True, null=True)
    activities = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    tg_alias = models.CharField(max_length=50, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    objects = CustomUserManager()

    # Use a unique related_name for the groups ManyToManyField
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='users_map',
        related_query_name='user',
    )

    # Use a unique related_name for the user_permissions ManyToManyField
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='users_map',
        related_query_name='user',
    )

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
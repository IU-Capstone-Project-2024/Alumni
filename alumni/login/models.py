from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=100, primary_key=True, serialize=False)

    def __str__(self):
        return self.name
    
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First name field must be set')
        if not last_name:
            raise ValueError('The Last name field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    user_photo = models.ImageField(upload_to='profile_pics/', blank=True)
    alias = models.CharField(max_length=50, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)
    activities = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email 
        
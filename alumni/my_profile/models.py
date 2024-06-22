from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to='profile_pics', blank=True, null=True, default="alumni/static/alumni/pictures/user_photo.png")
    graduation_year = models.IntegerField(default=2015)
    position = models.CharField(max_length=255, default='-')
    company = models.CharField(max_length=255, default='-')
    location = models.CharField(max_length=255, default='-')
    interests = models.TextField(blank=True, null=True)
    activities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

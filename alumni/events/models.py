from django.db import models
from django.utils.text import slugify

# Create your models here.

class Events(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    author_email = models.EmailField()
    author_name = models.CharField(max_length=100)
    author_surname = models.CharField(max_length=100)
    author_alias = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='event_pics/', default='event_pics/default_event_img.svg')
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    link = models.URLField(blank=True)
    tags = models.JSONField()

    def __str__(self):
        return f"{self.id}: {self.event_name}"

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = f'/events/{slugify(self.event_name)}'
        super().save(*args, **kwargs)

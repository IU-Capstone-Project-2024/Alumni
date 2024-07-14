from django.db import models
from django.utils.text import slugify
from login.models import Interest
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
    link = models.URLField(unique=True, blank=True)
    tags = models.ManyToManyField(Interest, related_name='events')

    def __str__(self):
        return f"{self.id}: {self.event_name}"

    def save(self, *args, **kwargs):
        if not self.link:
            slug = slugify(self.event_name)
            counter = 1
            while Events.objects.filter(link=f'/events/{slug}').exists():
                slug = f'{slug}-{counter}'
                counter += 1
            self.link = f'/events/{slug}'
        super().save(*args, **kwargs)

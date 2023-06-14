from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Event(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    unit_price = models.FloatField()
    sponsors = models.CharField(max_length=1000)
    image = models.ImageField(default='images.jpg', upload_to='event_images')
    slug = models.SlugField(max_length=300, blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.name)
        super().save()
    def get_nominees(self):
        return self.nominee_set.all()
    def __str__(self):
        return self.name

class Nominee(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=255)
    social_media = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='nominee_pictures')
    reason_for_filing = models.TextField()
    def __str__(self):
        return self.name
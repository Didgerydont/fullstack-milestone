import os
from django.db import models
from datetime import date, datetime
from django.utils.html import format_html
from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe


class PastSold(models.Model):
    name = models.CharField(max_length=254, default='')
    date_sold = models.DateTimeField(blank=True)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=15, decimal_places=2)
    finish_price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='images')
    edu_info = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name


class ItemRequest(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=999)
    budget = models.IntegerField()
    image = models.ImageField(upload_to='images', blank=True)
    externalURL = models.URLField(blank=True)
    contact = models.EmailField()
    request_date = models.DateTimeField(auto_now_add=True)

    #some of the code above and below is from https://teamtreehouse.com/community/django-display-imagefield-with-adminsiteregistermodelmymodel-trick

    def url(self):
        # returns a URL for either internal stored or external image url
        if self.externalURL:
            return self.externalURL
        else:
            # is this the best way to do this??
            return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.image)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

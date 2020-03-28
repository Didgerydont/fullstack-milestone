from django.db import models
from datetime import date, datetime
from django.utils.html import format_html
from django.contrib import admin


class PastSold(models.Model):
    name = models.CharField(max_length=254, default='')
    date_sold = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=15, decimal_places=2)
    finish_price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class ItemRequest(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=999)
    budget = models.IntegerField()
    image = models.ImageField(upload_to='media/images', blank=True, null=True)
    contact = models.EmailField()
    request_date = models.DateTimeField(auto_now_add=True)

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

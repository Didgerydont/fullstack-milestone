import os
from django.db import models
from datetime import date, datetime
from django.utils.html import mark_safe
from django.contrib import admin



class PastSold(models.Model):
    """
    Model for our past sold items to be displayed on the home page
    """
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
    """
    Item request model with function to allow us to see the picture in the admin panel
    """
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=999)
    budget = models.IntegerField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    contact = models.EmailField()
    request_date = models.DateTimeField(auto_now_add=True)

    def image_tag(self):

        return mark_safe('<img src="media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


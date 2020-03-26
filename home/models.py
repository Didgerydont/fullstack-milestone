from django.db import models
from datetime import date, datetime


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
    name = models.CharField(max_length=254, default='', required=True)
    description = models.TextField(max_length=999, required=True)
    budget = models.IntegerField(required=True)
    image = models.ImageField(upload_to='images', required=False)
    contact = models.EmailField(default='', required=True)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.fields import DateField, DateTimeField
from django.contrib.auth.models import User
from datetime import date, datetime

class Antiques(models.Model):
    name = models.CharField(max_length=254, default='')
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField(default='')
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_now_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    edu_info = models.TextField(default='')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name




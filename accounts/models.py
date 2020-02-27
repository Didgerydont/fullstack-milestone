from django.db import models
from phone_field import PhoneField

# User Model
class UserDetails(models.Model):
    firstname = models.CharField(max_length=56)
    lastname = models.CharField(max_length=45)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=45)
    post_code = models.CharField(max_length=45)
    country = models.CharField(max_length=45)

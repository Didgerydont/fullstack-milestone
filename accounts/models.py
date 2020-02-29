from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=56)
    lastname = models.CharField(max_length=45)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=45)
    post_code = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    birth_date = models.DateField(null=True, blank=True)
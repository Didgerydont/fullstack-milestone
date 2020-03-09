from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=56)
    lastname = models.CharField(max_length=45)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=45)
    post_code = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    birth_date = models.DateField(null=True, blank=True)
    AUTH_PROFILE_MODULE = 'app.Profile'
    
    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.userprofile.objects.create(user=instance)
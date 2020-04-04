from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    firstname = models.CharField(max_length=56, default='')
    lastname = models.CharField(max_length=45, default='')
    phone = models.CharField(max_length=14, default='')
    address = models.CharField(max_length=255, default='')
    town = models.CharField(max_length=45, default='')
    post_code = models.CharField(max_length=45, default='')
    country = models.CharField(max_length=45, default='')
    birth_date = models.DateField(null=True, blank=True)
    AUTH_PROFILE_MODULE = 'app.Profile'
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
from django.db import models


class Antiques(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_now_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

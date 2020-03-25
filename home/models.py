from django.db import models


class PastSold(models.Model):
    name = models.CharField(max_length=254, default='')
    date_sold = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    finish_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

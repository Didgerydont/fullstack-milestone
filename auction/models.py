from django.db import models
from django.contrib.auth.models import User
from antiques.models import Antiques


class Auction(models.Model):
    antique_id = models.ForeignKey(Antiques, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

    def __str__(self):
        return "AUCTION_ID:" + str(self.pk) + " ITEM_ID:" + str(self.auction_id)


class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + str(self.auction_id)   

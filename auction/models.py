from django.db import models
from django.contrib.auth.models import User
from antiques.models import Antiques


class Auction(models.Model):
    antiques = models.OneToOneField(Antiques, on_delete=models.CASCADE, primary_key=True)
    number_of_bids = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()
    current_leader = models.DecimalField(max_digits=15, decimal_places=2, default=0.01)
    winning_bidder = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    money_collected = models.BooleanField(default=False)
    auction_expired = models.BooleanField(default=False)

    def __str__(self):
        return "Antique:" + self.antiques.name


class WatchList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return "USER_ID:" + str(self.user_id)

class Bid(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()
    new_bid = models.DecimalField(max_digits=15, decimal_places=2, default=0.01)

    def __str__(self):
        return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + \
            str(self.auction_id) + " " + str(self.bid_time)
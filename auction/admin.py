from django.contrib import admin
from .models import Auction, WatchList, Bid

admin.site.register(Auction)
admin.site.register(WatchList)
admin.site.register(Bid)

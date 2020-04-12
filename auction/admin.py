from django.contrib import admin
from .models import Auction, WatchList, Bid



class AuctionAdmin(admin.ModelAdmin):
    list_display = ('antiques', 'time_starting', 'time_ending', 'winning_bidder', 'money_collected')
    list_filter = ('time_ending', 'time_starting', 'auction_expired')


admin.site.register(Auction, AuctionAdmin)
admin.site.register(WatchList)


class BidAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'auction_id', 'bid_time', 'new_bid')


admin.site.register(Bid, BidAdmin)

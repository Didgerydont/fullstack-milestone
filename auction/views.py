from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Auction, WatchList, Bid


@login_required
def add_to_watch_list(request, auction_id):
    """
    Adds an auction to the users watchlist
    """
    user = User.objects.filter(username=request.session['username'])
    auction = Auction.objects.filter(id=auction_id)
    watching = WatchList.objects.filter(auction_id=auction_id)
    if not watching:
        watchlist_item = WatchList()
        watchlist_item.auction_id = auction[0]
        watchlist_item.user_id = user[0]
        watchlist_item.save()
    else:
        watching.delete()
    return render(request, "antiques.html")

def bids(request):

    return render(request, "mybids.html")
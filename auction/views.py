from django.shortcuts import render
from .models import Auction, WatchList, Bid


def watch_list(request):
    
    return render(request, "mywatchlist.html")

def bids(request):

    return render(request, "mybids.html")
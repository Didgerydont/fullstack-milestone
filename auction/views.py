from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from .models import Auction, WatchList, Bid
from antiques.models import Antiques
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from auctioneer.config import pagination
from .forms import BidForm


def get_all_auctions(request):
    """
    Show all current auctions
    """
    auction = Auction.objects.all()
    pages = pagination(request, auction, 4)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'auction': auction
    }
    return render(request, "showallauctions.html", context)

def get_specific_auction(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    context = {
        'auction': auction
    }

    return render(request, 'auction.html', context)


def bid(request, pk):
    """
    Allow the user to join the Auction
    """
    if request.method == "POST":
        if request.user.is_authenticated:
            auction = get_object_or_404(Auction, pk=pk)
            if timezone.now() >= auction.time_starting and timezone.now() < auction.time_ending:
                bid = get_object_or_404(Bid, pk=pk)
                the_bid = Decimal(request.POST.get('bid'))
                    
                if auction.current_leader >= the_bid:
                    print('This bid is not high enough')
                    messages.error(request, "This bid is not high enough")

                else:
                    auction.current_leader = the_bid
                    auction.winning_bidder = request.user
                    bid.new_bid = the_bid
                    bid.antiques_id = auction.antiques
                    bid.auction_id = auction
                    bid.user_id = request.user
                    bid.auction_id.number_of_bids += 1
                    bid.bid_time = timezone.now()
                    bid.save()
                    auction.save()
                    messages.success(request, "Your bid amount has been updated!")

            else:
                messages.error(request, "Sorry, this item is either no longer up for auction or hasnt been put up yet")
   
        else:
            messages.error(request, "You must be registered to bid")
            
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def add_to_watch_list(request, auction_id):
    """
    Adds an auction to the users watchlist, not working currently
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
    return render(request, "mywatchlist.html")

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from antiques.models import Antiques
from django.contrib.auth.decorators import login_required
from .models import Auction, WatchList, Bid
from antiques.models import Antiques
from .forms import BidForm


def get_all_auctions(request):
    """
    Show all current auctions
    """
    auctions = Auction.objects.filter()
    context = {
        "auctions": auctions
    }

    return render(request, "showallauctions.html", context)


def auction(request, auction_id):
    """
    Display the item up for auction and the bidding form
    """
    get_auction = get_object_or_404(Auction, id=auction_id)
    antique = Auction.antiques.objects.get(
        name=request.antiques.auction.name,
        date_posted=request.antiques.auction.date_posted,
        description=request.antiques.auction.description,
        starting_price=request.antiques.auction.starting_price,
        buy_now_price=request.antiques.auction.buy_now_price,
        edu_info=request.antiques.auction.edu_info,
        image=request.antiques.auction.image,
    )
    bid = Bid.objects.filter(auction=auction_id)
    bid_form = BidForm()

    if auction.time_ending > timezone.now():
        if bid:
            new_bid = bid[0]
        
        else:
            bid_obj = Bid()
            bid_obj.user = get_object_or_404(User, id=1)
            bid_obj.get_auction = get_auction
            bid_obj.bid_time = get_auction.time_starting
            bid_obj.new_bid = 0.01
            bid_obj.save()
            new_bid = bid_obj

        if auction.time_starting < timezone.now():
            context = {
                'get_auction': get_auction,
                'antique': antique,
                'bid_form': bid_form
            }
        else:
            context = {
                    'get_auction': get_auction,
                    'new_bid': new_bid
                }
        return render(request, 'antiques.html', context)
    else:
        context = {
            'get_auction': get_auction
        }
    return render(request, 'auction.html', context)


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
    return render(request, "mywatchlist.html")

def bid(request):

    return render(request, "mybids.html")
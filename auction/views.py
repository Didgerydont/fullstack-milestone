from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.utils import timezone
from antiques.models import Antiques
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

@login_required
def auction(request, pk):
    """
    Allow the user to join the Auction
    """
    if request.method == "POST":
        if request.user.is_authenticated:
            antiques = get_object_or_404(Antiques, pk=id)
            auction_id = request.POST['auction_id']
            auction = Auction.objects.get(antiques)
            if timezone.now() >= auction.start_time and timezone.now() < auction.end_time:
               
                antiques = Antiques.objects.get(id=auction_id)
                bid = Bid()
                auction.current_leader = int(request.POST['bid'])
                    
                if auction.current_leader >= bid:
                    messages.error(request, "This bid is not high enough")

                else:
                    bid = bid.new_bid.request.POST['new_bid']
                    bid.antiques_id = antiques
                    bid.auction_id = auction
                    bid.user_id = request.user
                    bid.number_of_bids += 1
                    bid.bid_time = timezone.now()
                    bid.save()
                    auction.save()
                    messages.success(request, "Your bid amount has been updated!")

            else:
                messages.error(request, "Sorry, this item is either no longer up for auction or hasnt been put up yet")
   
        else:
            messages.error(request, "You must be registered to bid")
            
    return redirect(reverse('auction:get_all_auctions'))


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
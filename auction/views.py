from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from antiques.models import Antiques
from django.contrib.auth.decorators import login_required
from .models import Auction, WatchList, Bid
from .forms import BidForm




def auction(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    auction_item = Auction.objects.get(
        name=request.antiques.auction.name,
        date_posted=request.antiques.auction.date_posted,
        description=request.antiques.auction.description,
        starting_price=request.antiques.auction.starting_price,
        buy_now_price=request.antiques.auction.buy_now_price,
        edu_info=request.antiques.auction.edu_info,
        image=request.antiques.auction.image,
    )
    
    bid_form = BidForm()


    
    
    context = {
        'auction': auction,
        'bid_form': bid_form,
        'auction_item': auction_item
    }

    return render(request, 'antiques.html', context)


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
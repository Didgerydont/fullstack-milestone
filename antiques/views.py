from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Antiques
from auction.models import Auction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from auctioneer.config import pagination


def all_antiques(request):
    """
    Displays all products for sale that are currently active in the database
    """

    antiques = Antiques.objects.all()
    pages = pagination(request, antiques, 4)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'antiques': antiques,
    }

    return render(request, 'antiques.html', context)


def get_auction(request, pk):
    """
    Allows the user to go straight to the Auction for the specific item listed within the antiques page. 
    """
    auction = get_object_or_404(Auction, pk=pk)
    context = {
        'auction': auction
    }

    return render(request, 'auction.html', context)



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
    auction_information = Auction.objects.get(
        auction_id=request.antiques.auction.auction_id
    )
    pages = pagination(request, antiques, 4)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'antiques': antiques,
        'auction_information': auction_information
    }

    return render(request, 'antiques.html', context)



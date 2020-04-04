from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from antiques.models import Antiques
from auction.models import Auction
from home.models import PastSold
from auctioneer.config import pagination
from django.contrib import messages


def search_antiques(request):
    query = request.GET.get('q')

    if query:
        results = Antiques.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        results = Antiques.objects.all()
    pages = pagination(request, results, num=4)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
    }

    return render(request, "antiques.html", context)


def search_past_items(request):
    """
    Search through past sold items
    """
    query = request.GET.get('q')

    results = PastSold.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    pages = pagination(request, results, num=4)

    context = {
        'items': pages[0],
        'page_range': pages[1]
    }

    return render(request, "index.html", context)


def search_current_auctions(request):
    """
    Search through past sold items
    """
    query = request.GET.get('q')

    results = Auction.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    pages = pagination(request, results, num=4)

    context = {
        'items': pages[0],
        'page_range': pages[1]
    }

    return render(request, "showallauctions.html", context)
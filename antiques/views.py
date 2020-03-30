from django.shortcuts import render
from .models import Antiques
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
        'page_range': pages[1]
    }

    return render(request, 'antiques.html', context)

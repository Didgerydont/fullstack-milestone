from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.contrib import auth, messages
from .models import Antiques, Enquire
from .forms import EnquiryForm
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


def enquiry(request, pk):
    """
    Allows the user to make an enquiry on any of the items listed on the antiques page
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            antiques = get_object_or_404(Antiques, pk=pk)
            the_enquiry = request.POST.get('enquire-text')
            if request.method == 'POST':
                enquire = Enquire()
                enquire.user = request.user
                enquire.antiques = antiques
                enquire.enquiry = the_enquiry
                enquire.time_requested = timezone.now()
                enquire.save()
                messages.success(request, "Your enquiry has been recieved!")
        else:
            messages.error(request, "You must register in order to enquire about this item")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        



    
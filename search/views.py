from django.shortcuts import render, redirect, reverse
from antiques.models import Antiques
from home.models import PastSold
from django.db.models import Q
from django.contrib import messages


def search_antiques(request):
    """
    Search through current antiques
    """
    return render(request, "search_current.html")


def search_pastitems(request):
    """
    Search through past sold items
    """
    query = request.GET.get('q')

    results = PastSold.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    

    return render(request, "index.html", context)
from django.shortcuts import render, redirect
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
    if request.method == 'GET':
        items_search = request.GET.get('q')

        items_search = []

        if items_search is False or items_search == "":
            messages.error(request, 'You must enter a term to search')
            return redirect('index')

        else:
            check_for_matches = PastSold.objects.filter(Q(description__icontains=items_search))
            for item in check_for_matches:
                items_search.append(item)
            
    context = {
        'items_search': items_search
    }
    return render(request, "search_past.html", context)
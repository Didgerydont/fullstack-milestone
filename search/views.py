from django.shortcuts import render
from antiques.models import Antiques
from home.models import PastSold


def search_antiques(request):
    """
    Search through current antiques
    """
    found_antiques = Antiques.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search_current.html", {"found_antiques": found_antiques})


def search_pastitems(request):
    """
    Search through past sold items
    """
    found_pastitems = PastSold.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search_past.html", {"found_pastitems": found_pastitems})

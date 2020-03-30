from django.shortcuts import render
from .models import Antiques
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def all_antiques(request):
    """
    Displays all products for sale that are currently active in the database
    """
    antiques = Antiques.objects.all()
    paginator = Paginator(antiques, 10)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items

    context = {
        'antiques': antiques
    }

    return render(request, 'antiques.html', context)

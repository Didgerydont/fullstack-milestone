from django.shortcuts import render
from .models import Antiques


def all_antiques(request):
    """
    Displays all products for sale that are currently active in the database
    """
    antiques = Antiques.objects.all()
    return render(request, 'antiques.html', {'antiques': antiques})

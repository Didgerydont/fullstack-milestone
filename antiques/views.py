from django.shortcuts import render
from .models import Antiques


def all_products(request):
    antiques = Antiques.objects.all()
    return render(request, 'antiques.html', {'antiques': antiques})

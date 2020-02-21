from django.shortcuts import render
from .models import Antiques


def all_antiques(request):
    antiques = Antiques.objects.all()
    return render(request, 'antiques.html', {'antiques': antiques})

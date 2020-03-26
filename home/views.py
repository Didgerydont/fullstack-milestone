from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view that displays the Index page
    """
    return render(request, "index.html")


def displayPastProducts(request):
    """ Will display previously sold items on the home page """
    return render(request, "index.html")


def requestAnItem(request):
    """ Allows the user to place a request for an item not already listed on the site """
    return render(request, "requestAnItem.html")
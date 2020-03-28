from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from home.forms import RequestItemForm
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
    if request.method == 'POST':
        request_form = RequestItemForm(request.POST)
        if request_form.is_valid():
            request_form.save()
            messages.success(request, 'Your request was successfully updated!')
            print('success')
            return redirect(reverse('home:index'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        request_form = RequestItemForm(request.POST)
    context = {
        'request_form': request_form
    }
    return render(request, "requestAnItem.html", context)

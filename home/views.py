from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from home.forms import RequestItemForm
from home.models import PastSold
# Create your views here.


def index(request):
    """
    A view that displays the Index page
    """
    return render(request, "index.html")


def displayPastProducts(request):
    """ Will display previously sold items on the home page """
    past_sold = PastSold.objects.get(
        name=request.pastsold.name,
        date_sold=request.pastsold.date_sold,
        description=request.pastsold.description,
        starting_price=request.pastsold.starting_price,
        finish_price=request.pastsold.finish_price,
        image=request.pastsold.image,
        edu_info=request.pastsold.edu_info,
    )

    context = {
        'past_sold': past_sold
    }
    return render(request, "index.html", context)


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

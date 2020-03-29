from django.conf.urls import url, include
from .models import Auction, WatchList, Bid
from . import views
from .views import watch_list, bids


app_name = "auction"

urlpatterns = [
    url(r'watchlist$', views.watch_list, name="watch_list"),
    url(r'mybids$', views.bids, name="bids"),

]
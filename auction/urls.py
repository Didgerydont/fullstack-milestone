from django.conf.urls import url, include
from .models import Auction, WatchList, Bid
from . import views
from .views import add_to_watch_list, bids


app_name = "auction"

urlpatterns = [
    url(r'add_to_watch_list', views.add_to_watch_list, name="add_to_watch_list"),
    url(r'mybids', views.bids, name="bids"),

]
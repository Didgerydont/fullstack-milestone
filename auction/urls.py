from django.conf.urls import url, include
from .models import Auction, WatchList, Bid
from . import views
from .views import watch_list


app_name = "auction"

urlpatterns = [
    url(r'watchlist$', views.watch_list , name="watch_list")

]
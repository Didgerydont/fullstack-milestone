from django.conf.urls import url, include
from .models import Auction, WatchList, Bid
from . import views
from .views import auction, add_to_watch_list, get_all_auctions


app_name = "auction"

urlpatterns = [
    url(r'get_all_auctions/', views.get_all_auctions, name='get_all_auctions'),
    url(r'(?P<pk>\d+)/auction/', views.auction, name='auction'),
]
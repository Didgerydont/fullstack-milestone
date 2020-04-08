from django.conf.urls import url, include
from .models import Auction, WatchList, Bid
from . import views
from .views import bid, add_to_watch_list, get_all_auctions, get_specific_auction


app_name = "auction"

urlpatterns = [
    url(r'get_all_auctions/', views.get_all_auctions, name='get_all_auctions'),
    url(r'get_specific_auction/(?P<pk>\d+)/$', views.get_specific_auction, name='get_specific_auction'),
    url(r'bid/(?P<pk>\d+)$', views.bid, name='bid'),
    url(r'add_to_watch_list', views.add_to_watch_list, name='add_to_watch_list'),
]
from django.conf.urls import url, include
from .models import Auction, WatchList, Bid
from . import views
from .views import auction, add_to_watch_list, bid


app_name = "auction"

urlpatterns = [
    url(r'auction/<int:auction_id>/', views.auction, name='auction'),
    url(r'/bid/<int:auction_id>/', views.bid, name="bid"),
]
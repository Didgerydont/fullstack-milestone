from django.conf.urls import url, include
from .models import Auction, WatchList, Bid
from . import views
from .views import auction, add_to_watch_list, bid


app_name = "auction"

urlpatterns = [
    url(r'auction/<int:auction_id>/', auction, name='auction'),
    url(r'mybids/', views.bid, name="bid"),

]
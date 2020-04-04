from django.conf.urls import url
from . import views
from .views import search_antiques, search_past_items, search_current_auctions

app_name = 'search'

urlpatterns = [
    url('search/current_items', views.search_antiques, name='search_antiques'),
    url('search/search_past_items', views.search_past_items, name='search_past_items'),
    url('search/search_current_auctions', views.search_current_auctions, name='search_current_auctions'),
]

from django.conf.urls import url
from . import views
from .views import buy_now_checkout, checkout_auction


app_name = 'checkout'

urlpatterns = [
    url(r'^buy_now/(?P<pk>\d+)/$', views.buy_now_checkout, name='buy_now_checkout'),
    url(r'^checkout_auction/(?P<pk>\d+)/$', views.checkout_auction, name='checkout_auction'),   
]
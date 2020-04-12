from django.conf.urls import url, include
from . import views
from antiques.views import all_antiques


app_name = 'products'

urlpatterns = [
    url(r'antiques', views.all_antiques, name='antiques'),
    url(r'specific_auction/(?P<pk>\d+)/$', views.get_auction, name='get_auction'),
]
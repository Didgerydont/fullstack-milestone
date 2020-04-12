from django.conf.urls import url, include
from . import views
from antiques.views import all_antiques, enquiry


app_name = 'products'

urlpatterns = [
    url(r'antiques', views.all_antiques, name='antiques'),
    url(r'enquiry/(?P<pk>\d+)$', views.enquiry, name='enquiry'),
]
from django.conf.urls import url, include
from . import views
from antiques.views import all_antiques


app_name = 'products'

urlpatterns = [
    url(r'^$', views.all_antiques, name='antiques'),
]
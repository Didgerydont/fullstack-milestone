from django.conf.urls import url
from . import views
from home.views import requestAnItem


app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^requestAnItem/$', views.requestAnItem, name='requestAnItem'),
]

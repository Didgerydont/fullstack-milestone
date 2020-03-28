from django.conf.urls import url, include
from . import views
from home.views import requestAnItem
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^requestAnItem/$', views.requestAnItem, name='requestAnItem'),
]

urlpatterns += staticfiles_urlpatterns()

"""auctioneer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home import urls as urls_home
from antiques import urls as urls_antiques
from auction import urls as urls_auction
from search import urls as urls_search
from auction import urls as urls_auction
from checkout import urls as urls_checkout
from django.views import static
from . import settings
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(urls_home)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^antiques/', include(urls_antiques)),
    url(r'^search/', include(urls_search)),
    url(r'^auction/', include(urls_auction)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
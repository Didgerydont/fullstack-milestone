from django.conf.urls import url, include
from .views import all_antiques

urlpatterns = [
    url(r'^$', all_antiques, name='products'),
    
]
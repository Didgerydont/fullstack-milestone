from django.conf.urls import url
from .views import checkout


app_name = 'checkout'

urlpatterns = [
    url(r'^$', checkout, name='checkout'),  
]
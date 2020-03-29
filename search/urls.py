from django.conf.urls import url
from . import views
from .views import search_antiques, search_pastitems

app_name = 'search'

urlpatterns = [
    url('', views.search_antiques, name='search_antiques'),
    url('', views.search_pastitems, name='search_pastitems'),

]

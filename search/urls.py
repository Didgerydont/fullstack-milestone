from django.conf.urls import url
from . import views
from .views import search_antiques, search_pastitems

app_name = 'search'

urlpatterns = [
    url('search_antiques/', views.search_antiques, name='search_antiques'),
    url('search_pastitems/', views.search_pastitems, name='search_pastitems'),

]

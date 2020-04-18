from django.conf.urls import url, include
from . import views
from accounts.views import logout, login, registration, user_profile, edit_profile
from accounts import url_reset


app_name = 'accounts'

urlpatterns = [
    url(r'logout$', views.logout, name="logout"),
    url(r'login$', views.login, name="login"),
    url(r'register$', views.registration, name="register"),
    url(r'profile/', views.user_profile, name="profile"),
    url(r'(?P<pk>\d+)/profile_edit/$', views.edit_profile, name="edit_profile"),
    url(r'password-reset/', include(url_reset))
]
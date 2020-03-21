from django.conf.urls import url, include
from accounts import views
from accounts.views import logout, login, registration, user_profile, edit_profile, fucking_views
from accounts import url_reset


app_name = 'accounts'

urlpatterns = [
    url(r'logout$', views.logout, name="logout"),
    url(r'login$', views.login, name="login"),
    url(r'register$', views.registration, name="register"),
    url(r'profile$', views.user_profile, name="profile"),
    url(r'profile_edit/(?P<pk>\d+)/', views.edit_profile, name="edit_profile"),
    url(r'test$', views.fucking_views, name="fucking_views"),
    url(r'password-reset/', include(url_reset))
]
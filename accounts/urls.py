from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, edit_profile, fucking_views
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="register"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^profile_edit/(?P<user>\d+)/', edit_profile, name="edit_profile"),
    url(r'^test$', fucking_views, name="fucking_views"),
    url(r'password-reset/', include(url_reset))
    
]
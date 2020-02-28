from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile, update_user_information
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="register"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^profile-edit/', update_user_information, name="update-information"),
    url(r'password-reset/', include(url_reset))
]

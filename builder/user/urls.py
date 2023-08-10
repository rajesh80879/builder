from django.urls import path
from user.views import *

urlpatterns = [
    
    path("login", login_data, name="login-data"),
    path("", dashboard, name="dashboard"),
    path("contact/", contact, name="contact"),
    path("logout/", logout_user, name="logout"),

]
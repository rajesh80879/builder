from django.urls import path
from user.views import *

urlpatterns = [
    
    path("login", login_data, name="login-data"),
    path("", dashboard, name="dashboard"),
    path("contact/", contact, name="contact"),
    path("logout/", logout_user, name="logout"),

    path("about-us-background/", about_us_background, name="about-us-background"),
    path("about-us-management/", about_us_management, name="about-us-management"),
    path("projects/", projects, name="projects"),
    path("redevelopment-introduction/", redevelopment_introduction, name="redevelopment-introduction"),

]
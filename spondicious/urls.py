from django.urls import path
from .views import *   

urlpatterns = [
    path("", home_view, name="home"),
    # path("accounts/login/", login_view, name="login"),
]
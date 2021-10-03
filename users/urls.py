from django.contrib.auth.views import (LoginView, LogoutView)
from django.urls import path

from users.views import UserSignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("sign-up/", UserSignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout")
]

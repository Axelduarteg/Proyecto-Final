from django.urls import path
from .views import *

urlpatterns = [
    path("login/", login_request, name="login"),
    path('register/', register, name='register'),
    path("logout/", logout_request, name="logout"),
    path("LR/", LR, name="LR"),
    path('profile/', edit_user, name='edit_profile'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('user/<int:user_id>/edit/', edit_user, name='edit_user'),
    path("login/", login_request, name="login"),
    path('register/', register, name='register'),
    path("logout/", logout_request, name="logout"),
]
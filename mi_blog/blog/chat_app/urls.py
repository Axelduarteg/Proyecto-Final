from django.urls import path
from .views import *

urlpatterns = [
    path('chatroom/', chatroom, name='chatroom'),
]

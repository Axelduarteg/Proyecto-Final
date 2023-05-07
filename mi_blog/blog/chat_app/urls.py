from django.urls import path
from .views import *


urlpatterns=[
	

	path("dm/<str:username>", mensajes_privados),
	path("ms/<str:username>", DetailMs.as_view(), name="detailms"),

	path("", Inbox.as_view(), name="inbox"),

]
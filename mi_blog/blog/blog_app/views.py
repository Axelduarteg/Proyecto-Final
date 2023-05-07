from django.shortcuts import render
from accounts.models import Avatar
from django.conf import settings
import os

def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'blog_app/index.html', {'avatar':obtenerAvatar(request)})
    else:
        return render(request, 'blog_app/index.html')

def obtenerAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len (avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/default_avatar.jpg"


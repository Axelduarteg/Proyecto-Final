from django.shortcuts import render
from accounts.models import Avatar
from django.conf import settings
import os

def inicio(request):
    if request.user.is_authenticated:
        try:
            avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
        except (AttributeError, Avatar.DoesNotExist, IndexError):
            avatar = os.path.join(settings.MEDIA_URL, 'avatars', 'default_avatar.jpg')
        return render(request, 'blog_app/index.html', {'avatar': avatar})
    else:
        return render(request, 'blog_app/index.html')




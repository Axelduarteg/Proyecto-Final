from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars", default='default_avatar.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
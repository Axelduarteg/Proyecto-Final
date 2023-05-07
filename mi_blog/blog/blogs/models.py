from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='blog_imagen/', default='blog_imagen/default_imagen.jpg')

    def __str__(self):
        return self.title


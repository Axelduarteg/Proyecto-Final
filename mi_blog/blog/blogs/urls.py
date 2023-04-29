from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:blog_id>/update/', views.update, name='update'),
    path('<int:blog_id>/delete/', views.delete, name='delete'),
]
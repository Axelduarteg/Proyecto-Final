from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogs
from .forms import BlogsForm

def index(request):
    blogs = Blogs.objects.order_by('-created_at')
    context = {'blogs': blogs}
    return render(request, 'blogs_app/index.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs_app/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = BlogsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = BlogsForm()
    context = {'form': form}
    return render(request, 'blogs_app/create.html', context)

def update(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    if request.method == 'POST':
        form = BlogsForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', blog_id=blog_id)
    else:
        form = BlogsForm(instance=blog)
    context = {'form': form, 'blog': blog}
    return render(request, 'blogs_app/update.html', context)

def delete(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog:index')
    context = {'blog': blog}
    return render(request, 'blogs_app/delete.html', context)

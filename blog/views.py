from django.shortcuts import render
from .models import Blog, BlogCategory
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/index.html', {
        'blogs': blogs,
        'blog_categories': blog_categories
    })

def view(request, id):
    blog = Blog.objects.get(id=id)
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/view.html', {
        'blog': blog,
        'blog_categories': blog_categories
    })

def category(request, category_id):
    blogs = Blog.objects.all().filter(category_id=category_id)
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/index.html', {
        'blogs': blogs,
        'blog_categories': blog_categories
    })

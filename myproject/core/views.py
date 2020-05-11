from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-publication_date')
    data = {
        'post_list': posts
    }
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'sobre.html')

def detail(request, title):
    post = Post.objects.get(title=title)
    data = {
        'post': post
    }
    return render(request, 'detail.html', data)
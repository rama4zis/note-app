from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'posts/posts_list.html', { 'posts': posts })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', { 'post': post })


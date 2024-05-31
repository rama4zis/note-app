from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'posts/posts_list.html', { 'posts': posts })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', { 'post': post })

@login_required(login_url="/users/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save with user
            return redirect('posts:list')
    else:
        form = forms.CreatePost()

    # Add tailwindcss to Form
    form.fields['title'].widget.attrs['class'] = 'title w-full block mb-4 bg-gray-100 border border-gray-300 p-2 mb-4 outline-none'

    form.fields['content'].widget.attrs['class'] = 'description w-full block mb-4 bg-gray-100 sec p-3 h-60 border border-gray-300 outline-none'
    
    form.fields['slug'].widget.attrs['class'] = 'title w-full block mb-4 bg-gray-100 border border-gray-300 p-2 mb-4 outline-none'

    return render(request, 'posts/post_create.html', { 'form': form })
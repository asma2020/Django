from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
from django.http import HttpResponse, HttpResponseRedirect # pyright: ignore[reportMissingModuleSource]
from .models import Post, Comment
from .forms import PostForm

def index(requests):
    return HttpResponse('<h1> welcome to django </h1>')

def home(requests):
    return HttpResponse('<h3> welcome to myblog...!  </h3>')

def post_list(request):
    posts = Post.objects.all()
    context = { 'posts': posts}
    return render(request, 'posts/post_list.html', context=context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comment}
    return render(request,'posts/post_detail.html', context=context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data), form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()
    return render(request,'posts/post_create.html', {'form':form})

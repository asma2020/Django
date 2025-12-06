from django.shortcuts import render, get_object_or_404 # pyright: ignore[reportMissingModuleSource]
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound# pyright: ignore[reportMissingModuleSource]
from .models import Post, Comment
from .forms import PostForm
from django.views import generic # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .serializers import PostSerializer

@api_view(['GET','POST'])
def index(request):
    print(request.data)
    # return HttpResponse('<h1> welcome to django </h1>')
    pk = request.query_params.get('pk')
    print(request.query_params)
    try:
       p = Post.objects.get(pk=2)
    except Post.DoesNotExist:
        return Response({'detail': 'this post does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = PostSerializer(p)
    print('-'*100)
    print(serializer.data)
    return Response(serializer.data)

def home(requests):
    return HttpResponse('<h3> welcome to myblog...!  </h3>')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

def post_detail(request, post_id):
    # post = get_object_or_404(Post,pk= post_id)
    try:
       post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound('Post is not exist!')
    
    comment = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comment}
    return render(request,'posts/post_detail.html', context=context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    # context_object_name = 'posts'
    # def get_queryset(self):
    #     return get_object_or_404(Post,pk= self.request.POST['post_id'])
    def get_context_data(self, **kwargs):
       context = super(PostDetail, self).get_context_data()
       context['comments'] =  Comment.objects.filter(post= kwargs['object'].pk)
       return context
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

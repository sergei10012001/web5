from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {"posts" : posts})

class PostsDetail(DetailView):
    model = Post
    template_name = 'posts/detail_view.html'
    context_object_name = 'post'

class PostsUpdate(UpdateView):
    model = Post
    template_name = 'posts/create.html'
    context_object_name = 'post'
    form_class = PostForm

class PostsDelete(DeleteView):
    model = Post
    success_url = '/posts'
    context_object_name = 'post'
    template_name = 'posts/delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            error = 'incorrect input'
    form = PostForm()



    return render(request, 'posts/create.html', {'form' : form, 'error' : error})
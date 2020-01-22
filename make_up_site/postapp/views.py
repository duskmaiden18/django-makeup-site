from django.shortcuts import render,redirect
from .models import Post,Tag
from django.views import generic
from django.views import View
from .utils import *
from .forms import TagForm,PostForm
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    return render(request,'postapp/index.html',context={'posts':posts})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'postapp/post_detail.html'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request,'postapp/tags_list.html', context={'tags': tags})

class TagDetail(generic.DetailView):
    model = Tag
    template_name = 'postapp/tag_detail.html'

class TagCreate(ObjectCreateMixin,View):

    form_model = TagForm
    template = 'postapp/tag_create.html'

class PostCreate(ObjectCreateMixin,View):

    form_model = PostForm
    template = 'postapp/post_create.html'

class TagUpdate(ObjectUpdateMixin,View):

    model = Tag
    form_model = TagForm
    template = 'postapp/tag_update.html'

class PostUpdate(ObjectUpdateMixin,View):

    model = Post
    form_model = PostForm
    template = 'postapp/post_update.html'

class TagDelete(ObjectDeleteMixin,View):

    model = Tag
    template = 'postapp/tag_delete.html'
    redirect_url = 'postapp:tags_list'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'postapp/post_delete.html'
    redirect_url = 'postapp:posts_list'


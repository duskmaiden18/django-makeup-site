from django.shortcuts import render,redirect
from .models import Post,Tag
from django.views import generic
from django.views import View
from .forms import TagForm
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

class TagCreate(View):

    def get(self, request):
        form=TagForm()
        return render(request,'postapp/tag_create.html', context={'form':form})

    def post(self,request):
        bound_form=TagForm(request.POST)

        if bound_form.is_valid():
            new_tag=bound_form.save()
            return redirect(new_tag)
        return render(request,'postapp/tag_create.html',context={'form':bound_form})





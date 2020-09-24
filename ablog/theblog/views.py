from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post,Category
from .form import PostForm,editForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,ListView,DetailView,CreateView,DeleteView


# Create your views here.

""" def home(request):
    return render(request,'home.html',{})
 """
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    #fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = editForm
    template_name = 'editPost.html'
    #fields = ['title','title_tag','body']

class DetelePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')

class AddCategory(CreateView):
    model = Category
    template_name = 'addCategory.html'
    fields = '__all__'
    

from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy,reverse
from .models import Post,Category,Comment
from .form import PostForm,editForm,AddCommentForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,ListView,DetailView,CreateView,DeleteView
from django.http import HttpResponseRedirect

# Create your views here.

""" def home(request):
    return render(request,'home.html',{})
 """
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args,**kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        like = get_object_or_404(Post,id=self.kwargs['pk'])
        liked = False
        if like.likes.filter(id=self.request.user.id).exists():
            liked = True
        likes = like.total_likes()
        context['likes'] = likes
        context['liked'] = liked
        return context



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
    
def categoryViews(request,cats):
    Category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render (request,'category.html',{"cats":cats.title().replace('-',' '), "category_post":Category_posts})


class CategoryView(ListView):
    model = Category
    template_name = 'category_page.html'

def likeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('postLike'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("home:detail", args=(pk,)))


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    #fields = '__all__'
    template_name = 'add_comment.html'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home:home')




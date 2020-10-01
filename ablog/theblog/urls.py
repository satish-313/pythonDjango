from django.urls import path
from . import views
from .views import *

app_name = "home"

urlpatterns = [
    #path('',views.HomeView , name="HomeView")
    path('', HomeView.as_view() , name="home"),
    path('addPost/', AddPostView.as_view() , name="addPost"),
    path('article/<int:pk>' , ArticleDetailView.as_view() , name="detail"),
    path('article/edit/<int:pk>', UpdatePost.as_view() ,name="update" ),
    path('addCategory/', AddCategory.as_view() , name="addCategory"),
    path('article/delete/<int:pk>', DetelePost.as_view() ,name="delete" ),
    path('category/<str:cats>/', views.categoryViews,name="categoryViews"),
    path('category/', CategoryView.as_view(),name="category"),
    path('likes/<int:pk>', views.likeView, name="like_post"),
    path('article/<int:pk>/comment',AddCommentView.as_view(),name='add_comment')
]


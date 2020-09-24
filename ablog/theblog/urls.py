from django.urls import path
#from . import views
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
]
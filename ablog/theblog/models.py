from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('home:home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=60)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    body = RichTextField(blank=True,null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=300)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE, default=2)
    likes = models.ManyToManyField(User, related_name="blog_post")
    header_image = models.ImageField(null=True, blank=True , upload_to="image/")



    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse("home:detail", args= (self.id,))
        #return reverse('home:home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pics = models.ImageField(null=True, blank=True , upload_to="image/profile/")
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user}"
    
    def get_absolute_url(self):
    #return reverse("home:detail", args= (self.id,))
        return reverse('home:home')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} , {self.name}"


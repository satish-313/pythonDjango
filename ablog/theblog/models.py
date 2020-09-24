from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime,date

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
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE, default=2)


    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse("home:detail", args= (self.id,))
        #return reverse('home')
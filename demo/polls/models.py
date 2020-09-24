from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.TextField(null=True,blank=True)
    status = models.CharField(default='inacitive',max_length=64)
    created_by = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
    @property
    def choicess(self):
        return self.choice_set.all()

class choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    @property
    def votes(self):
        return self.answer_set.count()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = models.ForeignKey(choice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} : {self.choices.question}"

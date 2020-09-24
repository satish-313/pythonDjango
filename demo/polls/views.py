from django.shortcuts import render
from django.http import Http404,HttpResponse
from .models import *

# Create your views here.

def index(request):
    context = {}
    question = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = question
    return render(request,'polls/index.html',context)

def detail(request,id):
    context = {}
    try:
        question = Question.objects.get(pk = id)
    except:
        raise Http404
    context['question'] = question
    return render (request,"polls/detail.html",context)

def poll(request,id):
    if request.method == "GET":
        context = {}
        try:
            question = Question.objects.get(pk = id)
        except:
            raise Http404
        context['question'] = question
        return render(request,'polls/poll.html',context)
    if request.method == "POST":
        user_id = 1
        data = request.POST
        r = Answer.objects.create(user_id=user_id,choices_id=data["choice"])
        if r:
            return HttpResponse ("you vote is sumbit")
        else:
            return HttpResponse ("you vote is not sumbit")


from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .forms import userform,signUpForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context['error'] = "provide the valid credential"
            return render (request,'auth/login.html',context)
    else:
        return render (request,'auth/login.html',context)

def success(request):
    context = {}
    context
    return render(request,"auth/success.html",context)

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse("user_login"))

def employee_list(request):
    context = {}
    context['users'] = User.objects.all()
    return render(request,'employee/employee_list.html',context)

def employee_detail(request,id):
    context = {}
    context['user'] = get_object_or_404(User,id=id)
    return render (request,'employee/employee_detail.html',context)

def employee_add(request):
    form = signUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("employee_list"))
        else:
            return render(request,"employee/employee_add.html",{"user_form": form })
    else:
        return render(request,"employee/employee_add.html",{"user_form": form})

def employee_edit(request,id):
    user = get_object_or_404(User,id=id)
    if request.method == "POST":
        user_form = userform(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("employee_list"))
        else:
            return render(request,"employee/employee_edit.html",{"user_form":user_form})
    else:
        user_form = userform(instance=user)
        return render(request,"employee/employee_edit.html",{"user_form":user_form})

def employee_delete(request,id):
    user = get_object_or_404(User,id=id)
    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request,'employee/employee_delete.html',context)


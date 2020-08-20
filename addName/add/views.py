from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import name
from django.urls import reverse
# Create your views here.
def index(request):
    if request.method == "POST":
        addName = request.POST["name"]
        n = name(name=addName)
        n.save()
        #print("form submited")
        return HttpResponseRedirect(reverse("list"))
    return render (request, "add/index.html")

def list(request):
    listOfName = name.objects.all()
    return render (request,"add/list.html",{
        "list":listOfName
    })

def listItem(request,name_id):
    content = name.objects.get(pk = name_id)
    return render(request,"add/listItem.html",{
        "idNumber": content.id, "content": content.name
    })

def update(request,name_id):
    if request.method == "POST":
        updateName = request.POST["update"]
        listToUpdate = name.objects.get(pk = name_id)
        listToUpdate.name = updateName
        listToUpdate.save()
        return HttpResponseRedirect(reverse("list"))
    return render(request,"add/update.html",{
        "updateid":name_id
    })

def delete(request,name_id):
    listToDelete = name.objects.get(pk= name_id)
    listToDelete.delete()
    return HttpResponseRedirect(reverse("list"))
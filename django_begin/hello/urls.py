from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name = "index"),
    path("user", views.user , name = "brain"),
    #path("<str:name>", views.greet , name = "greet"),
    path("<str:name>", views.greets , name = "greets")
]
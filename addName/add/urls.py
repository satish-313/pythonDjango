from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/",views.list, name="list"),
    path("<int:name_id>/", views.listItem, name = "listItem"),
    path("<int:name_id>/delete/", views.delete , name = "delete"),
    path("<int:name_id>/update/", views.update , name = "update")
]
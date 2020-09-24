from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = "polls_list"),
    path('<int:id>detail/',views.detail ,name="detail"),
    path('<int:id>',views.poll,name="single_poll")
]
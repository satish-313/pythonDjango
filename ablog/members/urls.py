from django.urls import path
from .views import *

app_name = "signup"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]
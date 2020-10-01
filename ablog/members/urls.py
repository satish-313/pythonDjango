from django.urls import path
from .views import *
#from django.contrib.auth import views as auth_views

app_name = "signup"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UseEditView.as_view(), name='edit_profile'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'))
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('<int:pk>/edit_profile_page', editProfilePageView.as_view(), name="edit_profile_page"),
    path('<create_profile_page', CreateProfilePageView.as_view(), name="CreateProfilePageView"),


]
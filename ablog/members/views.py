from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .form import signUpForm,EditProfile,PasswordChangingForm,ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from theblog.models import Profile
# Create your views here.


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    #fields = '__all__'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


class editProfilePageView(generic.UpdateView):
    model = Profile
    fields = ['profile_pics','bio','linkedin_url']
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home:home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self,*args,**kwargs):
        #user = Profile.objects.all()
        context =super(ShowProfilePageView, self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class UserRegisterView(generic.CreateView):
    form_class = signUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UseEditView(generic.UpdateView):
    form_class = EditProfile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home:home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home:home')

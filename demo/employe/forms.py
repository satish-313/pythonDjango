from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name',
                   'email','username','password']
        
        #we can use the exclude some fields from main models form in django
        '''label = {
            'password' : 'Password'
        }
        def clean_email(self):
            if self.cleaned_data['email'].endsWith('@yourInstitudeName'):
                return self.cleaned_data['email']
            else:
                raise ValidationError("emial id not valid")
        
        def save(self):
            password = self.cleaned_data.pop('password')
            u = super().save()
            u.set_password(password)
            u.save()
            return u'''


class signUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')
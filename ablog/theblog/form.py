from django import forms
from .models import Post,Category,Comment

choice = Category.objects.all().values_list('name','name')

choice_list = []

for item in choice:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'Theuser','type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control','id':'Theuser'}),
            #'category': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),

        }

class editForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),

        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }


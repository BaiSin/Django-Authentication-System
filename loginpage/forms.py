from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'floatingUser', 'placeholder':'Smith John'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'floatingEmail', 'placeholder':'example@example.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'floatingPassword1', 'placeholder':'123'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'floatingPassword2', 'placeholder':'123'}))
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

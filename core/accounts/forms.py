from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter confirm password'}))

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']    
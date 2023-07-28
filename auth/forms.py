from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')



class LoginForm(AuthenticationForm):
    usrname = forms.CharField(max_length = 150)
    password = forms.CharField()
    
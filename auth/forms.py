from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length = 150)
    password = forms.CharField()
    
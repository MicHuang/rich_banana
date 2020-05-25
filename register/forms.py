from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser

class registerForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["phone", "email", "password1", "password2"]

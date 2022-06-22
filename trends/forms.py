from dataclasses import fields
import email
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['n_hood_id', 'title', 'post' , 'user', 'email']

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email', 'user' ]


    

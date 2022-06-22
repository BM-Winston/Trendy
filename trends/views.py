from django.shortcuts import redirect, render
from trends.forms import BusinessForm, RegisterForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import email
from .models import N_Hood, Post, Profile, Business
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()   

        return redirect('login')
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})


@login_required(login_url='/accounts/login/')
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('login')

@login_required(login_url='/accounts/login/')
def posts(request):

    post = Post.objects.all()
    return render(request,'post.html',{'post':posts})


@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('posts')
    else:
        form = PostForm()
    return render(request,'add_post.html',{'form':form})

@login_required(login_url='/accounts/login/')
def businesses(request):

    business = Business.objects.all()
    return render(request,'business.html',{'business':businesses})

@login_required(login_url='/accounts/login/')
def create_business(request):
    if request.method=='POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('businesses')
    else:
        form = BusinessForm()
    return render(request,'create_business.html',{'form':form})


@login_required(login_url='/accounts/login/')
def n_hood(request):

    n_hood = N_Hood.objects.all()
    return render(request,'n_hood.html',{' n_hood':n_hood})




from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'blog/home.html')


def user(request):
    return render(request, 'profile/profile.html')

from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'blog/home.html')


def user(request, user_id):
    users = User.objects.all()
    current_user = User.objects.get(id=user_id)
    context = { 'users': users, 'current_user': current_user }
    return render(request, 'profile/profile.html', context)

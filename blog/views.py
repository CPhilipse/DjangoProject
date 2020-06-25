from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'blog/home.html')


def user(request):
    users = User.objects.all()
    context = { 'users': users }
    # customer = Customer.objects.get(id=pk_test)
    return render(request, 'profile/profile.html', context)

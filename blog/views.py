from django.shortcuts import render
from .models import *


def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/home.html', context)


def article(request, pk):
    get_article = Article.objects.get(id=pk)
    author = get_article.user
    context = {'article': get_article, 'author': author}
    return render(request, 'blog/article.html', context)


def user(request, pk):
    users = User.objects.all()
    current_user = User.objects.get(id=pk)
    context = {'users': users, 'current_user': current_user}
    return render(request, 'profile/profile.html', context)

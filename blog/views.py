from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/home.html', context)


def article(request, article_id):
    # get_article = Article.objects.get(id=article_id)
    get_article = get_object_or_404(Article, id=article_id)
    comments = get_article.comments.filter(active=True)
    author = get_article.author
    context = {'article': get_article, 'author': author, 'comments': comments}
    return render(request, 'blog/article.html', context)


def user(request, user_id):
    users = User.objects.all()
    current_user = User.objects.get(id=user_id)
    context = {'users': users, 'current_user': current_user}
    return render(request, 'profile/profile.html', context)

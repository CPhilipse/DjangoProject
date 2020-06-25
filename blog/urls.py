from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user/<str:user_id>/', views.user),
    path('article/<str:article_id>/', views.article)
]

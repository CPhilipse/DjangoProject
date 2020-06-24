from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user/', views.user)
    # path('user/<str:user_id>/', views.user)
]
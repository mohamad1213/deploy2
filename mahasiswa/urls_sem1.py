from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views_sem1

urlpatterns = [
    path('', views_sem1.index_sem1),
    path('<id>/', views_sem1.detail),
    path('<id>/update/', views_sem1.update),
]

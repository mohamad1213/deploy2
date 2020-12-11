from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_sem1),
    path('<id>/', views.detail_dosen),
]

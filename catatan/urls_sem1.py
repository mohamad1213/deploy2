from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_dosen),
    path('new/', views.new),
    path('<id>/', views.detail_dosen),
    path('<id>/delete/', views.delete),
]

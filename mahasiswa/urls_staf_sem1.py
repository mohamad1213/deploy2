from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views_sem1
urlpatterns = [
    path('', views_sem1.index_staf),
    path('<id>/', views_sem1.detail_staf),
    path('<id>/delete/', views_sem1.delete_staf),
    # path('<id>/update/', views_sem1.update_staf),
    path('<id>/approve/', views_sem1.approve),
    # path('<id>/approve-batal/', views_sem1.approve_batal),
    path('<id>/reject/',views_sem1.reject),

]

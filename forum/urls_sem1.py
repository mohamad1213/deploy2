from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views_sem1


urlpatterns = [
    path('', views_sem1.index_sem1),
    path('<id>/', views_sem1.detail_forum_sem1),
    path('<id>/posting/<id_posting>/delete/', views_sem1.delete_posting_sem1),
    path('<id>/posting/<id_komen>/delete/komen', views_sem1.delete_komen_sem1),
    path('<id>/posting/<id_posting>/komen', views_sem1.sem1_komen),
    path('<id>/komen/<id_posting>/delete/', views_sem1.delete_komen_sem1),
]
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('cetak/', views.cetak),
    path('cetak_dosen/', views.cetak_dosen),
    path('cetak_staf/', views.cetak_staf),
    path('<id>/delete/', views.delete_catatan),
    path('cetak_dosen_sem1/', views.cetak_dosen_sem1),
    path('cetak_staf_sem1/', views.cetak_staf_sem1),
    path('<id>/delete/', views.delete_catatan),
]

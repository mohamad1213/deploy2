from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('cetak/', views.cetak),
    path('cetak_dosen/', views.cetak_dosen),
    path('cetak_staf/', views.cetak_staf),
    path('<id>/delete/', views.delete_catatan),
]

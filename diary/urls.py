from diary import views
from django.shortcuts import render
from django.urls import path
from django.views import generic

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view() ,name = 'index' ),
    path('', views.IndexView.as_view() ,name = 'base' ),
]

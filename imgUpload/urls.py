from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.imageUpload, name='imageUpload'),
    re_path(r'imageprocess', views.imageprocess, name= 'imageprocess')
]

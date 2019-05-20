from django.contrib import admin
from django.urls import re_path
from djangobin import views
from django.urls import path

urlpatterns = [
    path('index/',views.index, name='index'),
    re_path('user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile'),
    re_path('books/', views.book_category, name='books'),
    re_path(r'^books/(?P<category>[\w-]+)/$', views.book_category, name='books'),
    path('extra/', views.extra_args, {'arg1' : 1, 'arg2' : (10,20,30)}, name='extra_args'),
    path('custom-response/', views.custom_response),
    path('todayis/', views.today_is),
]
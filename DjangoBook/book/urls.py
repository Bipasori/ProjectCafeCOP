from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    url(r'^books/$', views.book_list, name='book_list'),
    #url(r'^books/create/$', views.book_create, name='book_create'),
    url(r'^create/$', views.book_create, name='book_create'),
    url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]

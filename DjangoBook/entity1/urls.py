from django.contrib import admin 
from django.urls import path 
from django.conf.urls import url, include 

from . import views 

urlpatterns = [ 
    url(r'^entity1/$', views.entity1_list, name='entity1_list'), 
    url(r'^entity1/create/$', views.entity1_create, name='entity1_create'), 
    url(r'^entity1/(?P<pk>\d+)/update/$', views.entity1_update, name='entity1_update'), 
    url(r'^entity1/(?P<pk>\d+)/delete/$', views.entity1_delete, name='entity1_delete'), 
] 

from django.conf.urls import url, include
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('myregister/', views.myregister, name="myregister"),
    path('mylogin/', views.mylogin, name="mylogin"),
    path('mylogout/', views.mylogout, name="mylogout"),
    path('test1/', views.test1, name="test1"),
]

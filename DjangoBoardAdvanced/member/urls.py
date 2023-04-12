from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('member_register', views.member_register, name="member_register"),
    path('member_idcheck', views.member_idcheck, name="member_idcheck"),
    path('member_insert', views.member_insert, name="member_insert"),
    path('member_login', views.member_login, name="member_login"),
    path('member_logout', views.member_logout, name="member_logout"),
    path('member_edit', views.member_edit, name="member_edit"),
    path('member_update', views.member_update, name="member_update"),
]

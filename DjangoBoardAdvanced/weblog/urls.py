from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('weblog', views.weblog, name="weblog"),
    path('weblog_front', views.weblog_front, name="weblog_front"),
]

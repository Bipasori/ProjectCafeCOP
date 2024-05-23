from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('coocr_upload', views.coocr_upload, name="coocr_upload"),
    ]

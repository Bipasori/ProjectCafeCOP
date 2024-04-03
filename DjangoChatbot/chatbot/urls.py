from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chattrain', views.chattrain, name="chattrain"),
    path('chatanswer', views.chatanswer, name="chatanswer"),
]

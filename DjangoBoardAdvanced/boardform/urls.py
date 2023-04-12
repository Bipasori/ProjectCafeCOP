from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('boardform', views.boardform, name="boardform"),
    path('boardform_create', views.boardform_create, name="boardform_create"),
    path('boardform_update', views.boardform_update, name="boardform_update"),
]

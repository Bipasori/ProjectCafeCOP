from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pdf, name='upload_pdf'),
    path('view/', views.view_pages, name='view_pages'),
    path('view2/', views.view_pages2, name='view_pages2'),
]
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('entitylist', views.entitylist, name='entitylist'),
    path('entity_create', views.entity_create, name='entity_create'),
    path('entity_config', views.entity_config, name='entity_config'),

    path('meta_create', views.meta_create, name='meta_create'),
    path('meta_read', views.meta_read, name='meta_read'),

    path('table_create', views.table_create, name='table_create'),
    path('codecreate_data', views.codecreate_data, name='codecreate_data'),
    path('codecreate_view', views.codecreate_view, name='codecreate_view'),
    path('codecreate_template', views.codecreate_template, name='codecreate_template'),
    path('codecreate_config', views.codecreate_config, name='codecreate_config'),
]

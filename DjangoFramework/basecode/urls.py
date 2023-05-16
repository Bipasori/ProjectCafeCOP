from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('codemanage', views.codemanage, name="codemanage"),
    path('codetype_insert', views.codetype_insert, name="codetype_insert"),
    path('codetype_update', views.codetype_update, name="codetype_update"),
    path('codetype_delete', views.codetype_delete, name="codetype_delete"),
    path('code_insert', views.code_insert, name="code_insert"),
    path('code_update', views.code_update, name="code_update"),
    path('code_delete', views.code_delete, name="code_delete"),
    path('code_view', views.code_view, name="code_view"),

    path('itemmanage', views.itemmanage, name="itemmanage"),
    path('itemtemplate_download', views.itemtemplate_download, name="itemtemplate_download"),
    path('itemdata_upload', views.itemdata_upload, name="itemdata_upload"),

    path('bommanage', views.bommanage, name="bommanage"),
    path('bom_create', views.bom_create, name="bom_create"),
    path('bomitem_read', views.bomitem_read, name="bomitem_read"),
    path('bomitem_pick', views.bomitem_pick, name="bomitem_pick"),
    path('bom_update', views.bom_update, name="bom_update"),

    path('apitest', views.apitest, name="apitest"),
]



from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("book.urls")),
    path('', include("nocode.urls")),
    path('', include("entity1.urls")),
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('accounts/', include('allauth.urls')),
    # path('', TemplateView.as_view(template_name="index.html")),
]

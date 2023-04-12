from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('', include('boardform.urls')),
    path('', include('album.urls')),
    path('', include('chart.urls')),
    path('', include('member.urls')),
    path('', include('weblog.urls')),
    path('graphql',
         csrf_exempt(GraphQLView.as_view(graphiql = True, schema = schema)),
    )
]

# https://github.com/graphql-python/graphene-django/issues/61
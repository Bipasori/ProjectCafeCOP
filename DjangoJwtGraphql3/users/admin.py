from django.contrib import admin
from .models import profile
from django.apps import apps

admin.site.register(profile)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
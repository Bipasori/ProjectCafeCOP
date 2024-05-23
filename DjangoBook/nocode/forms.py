from django import forms
from nocode.models import Entity

class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ('entity_name', 'status', )
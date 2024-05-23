from django import forms 
from entity1.models import Entity1 

class Entity1Form(forms.ModelForm): 
    class Meta: 
        model = Entity1 
        fields = ('id','Col001','Col002','Col003','Col004','Col005',) 
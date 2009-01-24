from django.forms import ModelForm
from models import Case, Script

class UpdateCaseForm(ModelForm):
    
    class Meta:
        model = Case
        fields = ('script', 'source', 'use_qunit')
    
    def process(self, request): 
        self.save()
from django.forms import ModelForm
from models import Case

class UpdateCaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ('script', 'source')
    
    def process(self, request):
        self.save()


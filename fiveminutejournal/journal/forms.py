from django.forms import ModelForm
from journal.models import Morning

class MorningForm(ModelForm):
    class Meta:
        model = Morning
        fields = '__all__'

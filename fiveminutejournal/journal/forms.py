from django.forms import ModelForm
from journal.models import Morning, Evening

class MorningForm(ModelForm):
    class Meta:
        model = Morning
        fields = '__all__'

class EveningForm(ModelForm):
    class Meta:
        model = Evening
        fields = '__all__'

from django import forms
from .models import Morning, Evening, GoalCategory
from django.contrib.admin.widgets import AdminDateWidget


class MorningForm(forms.ModelForm):
    class Meta:
        model = Morning
        fields = '__all__'


class EveningForm(forms.ModelForm):
    class Meta:
        model = Evening
        fields = '__all__'


class GoalForm(forms.Form):
    new_goal_text = forms.CharField(label='New Goal', max_length=200)
    category = forms.ModelChoiceField(queryset=GoalCategory.objects.all())


class EventForm(forms.Form):
    text = forms.CharField(label='New Event', max_length=200)
    date = forms.DateField(label='Event Date (mm/dd/yyyy)', widget=AdminDateWidget)


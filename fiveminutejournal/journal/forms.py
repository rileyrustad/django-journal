from django import forms
from .models import Morning, Evening, GoalCategory


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



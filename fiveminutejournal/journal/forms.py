from django import forms
from .models import GoalCategory, Journal
from django.contrib.admin.widgets import AdminDateWidget


class JournalForm(forms.Form):
    def __init__(self, journal_id, *args, **kwargs):
        j = Journal.objects.filter(pk=journal_id)[0]
        super(JournalForm, self).__init__(*args, **kwargs)
        for question in j.question_set.all():
            for i in range(question.responses_number):
                name = 'question' + question.text + str(i)
                self.fields[name] = forms.CharField()
                if i == 0:
                    self.fields[name].label = question.text
                else:
                    self.fields[name].label = ''
        self.fields['additional_answer'] = forms.CharField(widget=forms.Textarea)
        self.fields['additional_answer'] = 'Additional Answer'


class GoalForm(forms.Form):
    new_goal_text = forms.CharField(label='New Goal', max_length=200)
    category = forms.ModelChoiceField(queryset=GoalCategory.objects.all())


class EventForm(forms.Form):
    text = forms.CharField(label='New Event', max_length=200)
    date = forms.DateField(label='Event Date (mm/dd/yyyy)', widget=AdminDateWidget)


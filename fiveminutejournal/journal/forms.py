from django import forms
from django.contrib.auth.models import User
from .models import GoalCategory, Journal
from django.contrib.admin.widgets import AdminDateWidget


class JournalForm(forms.Form):
    def __init__(self, journal_name, *args, **kwargs):
        j = Journal.objects.filter(name=journal_name)[0]
        super(JournalForm, self).__init__(*args, **kwargs)
        for question in j.question_set.all():
            for i in range(question.responses_number):
                name = str(question.id) + ' question ' + question.text + ' ' + str(i)
                self.fields[name] = forms.CharField()
                if i == 0:
                    self.fields[name].label = question.text
                else:
                    self.fields[name].label = ''
        self.fields['additional_answer'] = forms.CharField(widget=forms.Textarea)
        self.fields['additional_answer'].label = 'Additional Reflection'


class ArchiveForm(forms.Form):
    start_date = forms.DateField(label='Start Date:')
    end_date = forms.DateField(label='End Date:')


class GoalForm(forms.Form):
    new_goal_text = forms.CharField(label='New Goal', max_length=200)
    category = forms.ModelChoiceField(queryset=GoalCategory.objects.all())


class EventForm(forms.Form):
    text = forms.CharField(label='New Event', max_length=200)
    date = forms.DateField(label='Event Date (mm/dd/yyyy)', widget=AdminDateWidget)


class CompletedGoalForm(forms.Form):
    def __init__(self, journal_user, *args, **kwargs):
        goal_cats = journal_user.goalcategory_set.all()
        super(CompletedGoalForm, self).__init__(*args, **kwargs)
        for goal_cat in goal_cats:
            for goal in goal_cat.goal_set.all():
                if goal.active == True:
                    self.fields[str(goal.id)] = forms.BooleanField()
                    self.fields[str(goal.id)].label = goal.text
                    self.fields[str(goal.id)].required = False

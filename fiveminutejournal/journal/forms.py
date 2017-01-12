from django import forms
from django.contrib.auth.models import User
from .models import GoalCategory, Journal, Response
from django.contrib.admin.widgets import AdminDateWidget
from .models import JournalSettings


class EntryForm(forms.Form):
    def __init__(self, journal_name, *args, **kwargs):
        j = Journal.objects.filter(name=journal_name)[0]
        super(EntryForm, self).__init__(*args, **kwargs)
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

class DeletedGoalForm(forms.Form):
    def __init__(self, journal_user, *args, **kwargs):
        goal_cats = journal_user.goalcategory_set.all()
        super(DeletedGoalForm, self).__init__(*args, **kwargs)
        for goal_cat in goal_cats:
            for goal in goal_cat.goal_set.all():
                if goal.active == False:
                    self.fields[str(goal.id)] = forms.BooleanField()
                    self.fields[str(goal.id)].label = goal.text
                    self.fields[str(goal.id)].required = False

class EditEntryForm(forms.Form):
    def __init__(self, response_id, *args, **kwargs):
        response = Response.objects.filter(pk=response_id)[0]
        super(EditEntryForm, self).__init__(*args, **kwargs)
        answers = response.answer_set.all()
        additional_answer = response.additionalanswer_set.all()[0]

        for answer in answers:
            self.fields[str(answer.id)] = forms.CharField()
            self.fields[str(answer.id)].label = answer.question
            self.fields[str(answer.id)].initial = answer.text

        self.fields['additional_answer'] = forms.CharField(widget=forms.Textarea)
        self.fields['additional_answer'].label = 'Additional Reflection'
        self.fields['additional_answer'].initial = additional_answer.text


class JournalSettingsForm(forms.ModelForm):
    class Meta:
        model = JournalSettings
        fields = ['first_name', 'last_name', 'goals', 'events']


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['name', 'journal_type']


class GoalCategoryForm(forms.ModelForm):
    class Meta:
        model = GoalCategory
        fields = ['text']
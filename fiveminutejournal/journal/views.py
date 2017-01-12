from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .forms import GoalForm, EventForm, EntryForm, ArchiveForm, CompletedGoalForm, DeletedGoalForm, EditEntryForm, JournalSettingsForm, JournalForm, GoalCategoryForm
from .models import GoalCategory, Goal, Journal, Event, Answer, Response, Question, AdditionalAnswer, JournalSettings
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import inlineformset_factory


def index(request):
    goals = []
    events = []
    first_journal = []
    middle_journals = []
    last_journal = []
    response_exists = False
    responses = []
    week_responses = []
    goals_default = False
    events_default = False
    journals_defualt = False
    try:
        settings = User.objects.filter(pk=request.user.id)[0].journalsettings
    except:
        settings = JournalSettings(user=request.user)
        settings.save()

    if request.user.is_authenticated:
        goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()
        events = User.objects.filter(pk=request.user.id)[0].event_set.filter(date__gte=timezone.datetime.now()).order_by('date')
        first_journal = User.objects.filter(pk=request.user.id)[0].journal_set.filter(journal_type='F').exclude(response__date=timezone.datetime.now().date())
        middle_journals = User.objects.filter(pk=request.user.id)[0].journal_set.filter(journal_type='M').exclude(response__date=timezone.datetime.now().date())
        last_journal = User.objects.filter(pk=request.user.id)[0].journal_set.filter(journal_type='L').exclude(response__date=timezone.datetime.now().date())
        responses = User.objects.filter(pk=request.user.id)[0].response_set.filter(date=timezone.datetime.now().date())
        today = timezone.now()
        week_responses = User.objects.filter(pk=request.user.id)[0].response_set.filter(date__gte=timezone.now() - timezone.timedelta(days=today.weekday()))
        journals = User.objects.get(pk=request.user.id).journal_set.all()

    if len(goals) == 0:
        goals_default = True
    if len(events) == 0:
        events_default = True
    if len(journals) == 0:
        journals_defualt = True


    if len(responses) > 0:
        response_exists = True
    context = {
        'goals': goals,
        'events': events,
        'morning': 'morning',
        'evening': 'evening',
        'response_exists': response_exists,
        'responses': responses,
        'first_journal': first_journal,
        'middle_journals': middle_journals,
        'last_journal': last_journal,
        'week_responses': week_responses,
        'settings': settings,
        'goals_default': goals_default,
        'events_default': events_default,
        'journals_default': journals_defualt,

    }
    return render(request, 'index.html', context)


def complete(request):
    goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()
    events = User.objects.filter(pk=request.user.id)[0].event_set.filter(date__gte=timezone.now()).order_by('date')
    context = {
        'goals': goals,
        'events': events,
    }
    return render(request, 'entry_complete.html', context)


def entry(request, journal_name):
    goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()
    events = User.objects.filter(pk=request.user.id)[0].event_set.filter(date__gte=timezone.now()).order_by('date')
    name = ''
    entry_type_first = False
    entry_type_middle = False
    entry_type_last = False
    for journal in Journal.objects.all():
        if journal_name == journal.name:
            response = Response(journal_type=journal, date=timezone.now(), user=request.user)
            form = EntryForm(journal.name, request.POST)

            if journal.journal_type == 'F':
                entry_type_first = True
            elif journal.journal_type == 'M':
                entry_type_middle = True
            elif journal.journal_type == 'L':
                entry_type_last = True
            name = journal.name
            continue

    if request.method == 'POST':
        if form.is_valid():
            response.save()
            for answer in form.cleaned_data:
                if 'question' in answer:
                    id = [int(s) for s in answer.split() if s.isdigit()][0]
                    q = Question.objects.filter(id=id)[0]
                    a = Answer(text=form.cleaned_data[answer], response=response, question=q)
                    a.save()
                if 'additional_answer' in answer:
                    a = AdditionalAnswer(text=form.cleaned_data[answer], response=response)
                    a.save()
            return HttpResponseRedirect('/journal/entry/complete')
    else:
        form = EntryForm(journal_name=name)
        response_exists = False
        responses = Response.objects.filter(date=timezone.now().date())
        if len(responses) > 0:
            response_exists = True
        context = {
            'form': form,
            'events': events,
            'goals': goals,
            'responses': responses,
            'response_exists': response_exists,
            "entry_type_first": entry_type_first,
            "entry_type_middle": entry_type_middle,
            "entry_type_last": entry_type_last,
            "entry_type_morning": True,
            'journal_name':journal_name


        }
        return render(request, 'entry.html', context)


def goals(request):
    goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()
    events = User.objects.filter(pk=request.user.id)[0].event_set.filter(date__gte=timezone.now()).order_by('date')
    if request.method == 'POST':
        form = GoalForm(data=request.POST, user=request.user)
        if form.is_valid():
            text = form.cleaned_data['new_goal_text']
            category = form.cleaned_data['category']
            g = Goal(text=text, category=category)
            g.save()
            return HttpResponseRedirect('/journal/')
    else:
        form = GoalForm(user=request.user)
    context = {
        'form': form,
        'events': events,
        'goals': goals,
    }
    return render(request, 'goals.html', context)


def events(request):
    goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()
    events = User.objects.filter(pk=request.user.id)[0].event_set.filter(date__gte=timezone.now()).order_by('date')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            date = form.cleaned_data['date']
            e = Event(text=text, date=date, user=request.user)
            e.save()
            return HttpResponseRedirect('/journal/')
    else:
        form = EventForm()
    context = {
        'form': form,
        'events': events,
        'goals': goals,
    }
    return render(request, 'events.html', context)


def archive(request, start_date):
    now = timezone.now().date()
    week = str(now - timezone.timedelta(days=7))
    month = str(now - timezone.timedelta(days=31))
    year = str(now - timezone.timedelta(days=365))

    context = {
        'now': now,
        'week': week,
        'month': month,
        'year': year,
    }

    if start_date == 'home':
        return render(request, 'archive.html', context)
    elif start_date == 'all':
        responses = User.objects.filter(pk=request.user.id)[0].response_set.all().order_by('-date')
        context['responses'] = responses
        return render(request, 'archive.html', context)
    else:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        responses = User.objects.filter(pk=request.user.id)[0].response_set.filter(date__gte=start_date).order_by('-date')
        context['responses'] = responses
        return render(request, 'archive.html', context)


def completed_goals(request):
    goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()

    if request.method == 'POST':
        form = CompletedGoalForm(journal_user=request.user, data=request.POST)
        if form.is_valid():
            for answer in form.cleaned_data:
                if form.cleaned_data[answer]:
                    goal = Goal.objects.filter(id=int(answer))[0]
                    goal.active = False
                    goal.save()
            return HttpResponseRedirect('/journal/')

        else:
            return HttpResponseRedirect('/')
    else:
        form = CompletedGoalForm(journal_user=request.user)

    context = {
        'goals': goals,
        'form': form,
    }
    return render(request, 'completedGoals.html', context)


def deleted_goals(request):
    goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()

    if request.method == 'POST':
        form = DeletedGoalForm(journal_user=request.user, data=request.POST)
        if form.is_valid():
            for answer in form.cleaned_data:
                if form.cleaned_data[answer]:
                    goal = Goal.objects.filter(id=int(answer))[0]
                    goal.active = True
                    goal.save()
            return HttpResponseRedirect('/journal/')
    else:
        form = DeletedGoalForm(journal_user=request.user)

    context = {
        'goals': goals,
        'form': form,
    }
    return render(request, 'deletedGoals.html', context)


def edit_entry(request, response_id):
    response = Response.objects.filter(pk=response_id)[0]
    if request.method == 'POST':
        form = EditEntryForm(response_id=response_id, data=request.POST)
        if form.is_valid():
            for answer in form.cleaned_data:
                if answer == 'additional_answer':
                    additional_answer = response.additionalanswer_set.all()[0]
                    additional_answer.text = form.cleaned_data[answer]
                    additional_answer.save()
                else:
                    revised_answer = Answer.objects.filter(pk=int(answer))[0]
                    revised_answer.text = form.cleaned_data[answer]
                    revised_answer.save()


            return HttpResponseRedirect('/journal/')

    else:
        form = EditEntryForm(response_id=response_id)
    context = {
        'response': response,
        'form': form,
    }
    return render(request, 'editEntry.html', context)

def journal_settings(request):
    settings = User.objects.filter(pk=request.user.id)[0].journalsettings
    journals = User.objects.filter(pk=request.user.id)[0].journal_set.all()
    if request.method == 'POST':
        new_settings = JournalSettingsForm(data=request.POST, instance=settings)
        if new_settings.is_valid():
            new_settings.save()
        return HttpResponseRedirect('/journal/')

    else:
        form = JournalSettingsForm(instance=settings)
    new_journal = Journal.objects.count()
    print(new_journal, 'blah')
    context = {
        'journals': journals,
        'form': form,
        'new_journal': new_journal,
    }
    return render(request, 'journal_settings.html', context)


def edit_journal(request, journal_id):
    if journal_id == 'new':
        journal = Journal(user=request.user, name="New Journal")
        journal.save()
        return HttpResponseRedirect('/journal/settings/')
    else:
        journal = Journal.objects.get(pk=journal_id)

    QuestionInlineFormSet = inlineformset_factory(Journal, Question, fields=('text', 'responses_number'))
    if request.method == "POST":
        formset = QuestionInlineFormSet(request.POST, request.FILES, instance=journal)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/journal/')
    else:
        formset = QuestionInlineFormSet(instance=journal)
    new_journal = Journal.objects.count()
    context = {
        'journal': journal,
        'formset': formset,
        'new_journal': new_journal,
    }
    return render(request, 'editJournal.html', context)


def edit_journal_name(request, journal_id):
    journal = User.objects.filter(pk=request.user.id)[0].journal_set.get(pk=journal_id)
    if request.method == 'POST':
        j = JournalForm(data=request.POST, instance=journal)
        if j.is_valid():
            j.save()
        return HttpResponseRedirect('/journal/')

    else:
        form = JournalForm(instance=journal)
    not_new = True
    if journal_id == 'new':
        not_new = False
    context = {
        'journal': journal,
        'form': form,
        'not_new': not_new
    }
    return render(request, 'editJournalName.html', context)


def edit_goal_category(request, goal_cat_id):
    if goal_cat_id == 'new':
        g = GoalCategory(user=request.user, text="New Category (rename here --->)")
        g.save()
        return HttpResponseRedirect('/journal/goal_categories/')
    goal_cat = User.objects.get(pk=request.user.id).goalcategory_set.get(pk=goal_cat_id)
    if request.method == 'POST':
        g = GoalCategoryForm(data=request.POST, instance=goal_cat)
        if g.is_valid():
            g.save()
        return HttpResponseRedirect('/journal/')

    else:
        form = GoalCategoryForm(instance=goal_cat)
    context = {
        'goal_cat': goal_cat,
        'form': form,
    }
    return render(request, 'editGoalCat.html', context)


def goal_categories(request):
    categories = User.objects.get(pk=request.user.id).goalcategory_set.filter(active=True)
    return render(request, 'goalCategories.html', {'categories':categories})


def delete_journal(request, journal_id):
    j = Journal.objects.get(pk=journal_id)
    j.delete()
    return HttpResponseRedirect('/journal/settings/')


def delete_response(request, response_id):
    r = Response.objects.get(pk=response_id)
    r.delete()
    return HttpResponseRedirect('/journal/archive/home/')


def delete_goal(request, goal_id):
    g = Goal.objects.get(pk=goal_id)
    g.delete()
    return HttpResponseRedirect('/journal/')


def delete_event(request, event_id):
    e = Event.objects.get(pk=event_id)
    e.delete()
    return HttpResponseRedirect('/journal/')


def delete_goal_category(request, goal_cat_id):
    g = GoalCategory.objects.get(pk=goal_cat_id)
    g.delete()
    return HttpResponseRedirect('/journal/goal_categories')


def journal_defaults(request):
    user = User.objects.get(pk=request.user.id)
    morning = Journal(user=user, journal_type='F', name='Morning')
    morning.save()
    q1 = Question(text='I am grateful for...', journal=morning, responses_number=3).save()
    q2 = Question(text='What would make today great?', journal=morning, responses_number=3).save()
    q3 = Question(text='Daily affirmations. I am...', journal=morning, responses_number=2).save()

    evening = Journal(user=user, journal_type='L', name='Evening')
    evening.save()
    q4 = Question(text='3 amazing things that happened today...', journal=evening, responses_number=3).save()
    q5 = Question(text='How could I have made today better?', journal=morning, responses_number=2).save()
    return HttpResponseRedirect('/journal/')


def goal_defaults(request):
    user = User.objects.get(pk=request.user.id)
    ff = GoalCategory(user=user, text='Family/Friend Goals')
    ff.save()
    Goal(category=ff, text="Call a Friend that you haven't spoken to in over a year").save()
    health = GoalCategory(user=user, text='Health Goals')
    health.save()
    Goal(category=health, text="Go to the gym 3 times this week").save()
    edu = GoalCategory(user=user, text='Educational Goals')
    edu.save()
    Goal(category=edu, text="Learn to cook something you've never made before").save()
    work = GoalCategory(user=user, text='Professional Goals')
    work.save()
    Goal(category=work, text="Each day this week start with the most important task").save()
    return HttpResponseRedirect('/journal/')


def event_defaults(request):
    today = timezone.now().date()
    year = today.year
    fourth = timezone.datetime(year, 7, 4).date()
    xmas = timezone.datetime(year, 12, 25).date()
    if today > fourth:
        fourth = timezone.datetime(year+1, 7, 4).date()
    if today > xmas:
        xmas = timezone.datetime(year+1, 7, 4).date()
    Event(text='Independence Day', date=timezone.datetime(2017, 7, 4), user=request.user).save()
    Event(text='Christmas Day', date=timezone.datetime(2017, 12, 25), user=request.user).save()
    #TODO: Add all US holidays, even the ones that have varying dates.


    return HttpResponseRedirect('/journal/')



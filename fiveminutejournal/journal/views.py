from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .forms import GoalForm, EventForm, JournalForm
from .models import GoalCategory, Goal, Journal, Event, Answer, Response, Question, AdditionalAnswer
from django.contrib.auth.models import User


def index(request):
    goals = []
    events = []
    first_journal = []
    middle_journals = []
    last_journal = []
    response_exists = False
    responses = []

    if request.user.is_authenticated:
        goals = User.objects.filter(pk=request.user.id)[0].goalcategory_set.all()
        events = User.objects.filter(pk=request.user.id)[0].event_set.filter(date__gte=timezone.now()).order_by('date')
        first_journal = User.objects.filter(pk=request.user.id)[0].journal_set.filter(journal_type='F').exclude(response__date=timezone.now().date())
        middle_journals = User.objects.filter(pk=request.user.id)[0].journal_set.filter(journal_type='M').exclude(response__date=timezone.now().date())
        last_journal = User.objects.filter(pk=request.user.id)[0].journal_set.filter(journal_type='L').exclude(response__date=timezone.now().date())
        responses = User.objects.filter(pk=request.user.id)[0].response_set.filter(date=timezone.now().date())

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
            form = JournalForm(journal.name, request.POST)

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
        form = JournalForm(journal_name=name)
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
        form = GoalForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['new_goal_text']
            category = form.cleaned_data['category']
            g = Goal(text=text, category=category)
            g.save()
            return HttpResponseRedirect('/journal/')
    else:
        form = GoalForm()
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
            e = Event(text=text, date=date)
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

def archive(request, date):
    if date == 'home':
        context = {}
        return render(request, 'archive.html', context)


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .forms import GoalForm, EventForm, JournalForm
from .models import GoalCategory, Goal, Journal, Event, Answer, Response, Question, AdditionalAnswer


def index(request):
    goals = GoalCategory.objects.all()
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    journals = Journal.objects.all()
    context = {
        'goals': goals,
        'events':events,
        'morning':'morning',
        'evening':'evening',
        'journals':journals,
    }
    return render(request, 'index.html', context)


def complete(request):
    goals = GoalCategory.objects.all()
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    context = {
        'goals': goals,
        'events': events,
    }
    return render(request, 'entry_complete.html', context)


def entry(request, journal_name):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    goals = GoalCategory.objects.all()
    name =''
    for journal in Journal.objects.all():
        if journal_name == journal.name:
            response = Response(journal_type=journal, date=timezone.now())
            form = JournalForm(journal.name, request.POST)
            entry_type_first = False
            entry_type_middle = False
            entry_type_last = False
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
                    q = Question.objects.filter(id=answer[0])[0]
                    a = Answer(text=form.cleaned_data[answer], response=response, question=q)
                    a.save()
                if 'additional_answer' in answer:
                    a = AdditionalAnswer(text=form.cleaned_data[answer], response=response)
                    a.save()
            return HttpResponseRedirect('/journal/entry/complete')
    else:
        form = JournalForm(journal_name=name)
    context = {
        'form': form,
        'events': events,
        'goals': goals,
        "entry_type_first" : entry_type_first,
        "entry_type_middle" : entry_type_middle,
        "entry_type_last" : entry_type_last,
        "entry_type_morning": True
    }
    return render(request, 'entry.html', context)


def goals(request):
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

    return render(request, 'goals.html', {'form': form})


def events(request):
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

    return render(request, 'events.html', {'form': form})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .forms import GoalForm, EventForm, JournalForm
from .models import GoalCategory, Goal, Event


def index(request):
    goals = GoalCategory.objects.all()
    events = Event.objects.filter(date__gte=timezone.now()).order_by('-date')
    context = {
        'goals': goals,
        'events':events,
    }
    return render(request, 'index.html', context)


def morning(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('-date')
    goals = GoalCategory.objects.all()
    if request.method == 'POST':
        form = JournalForm(1, request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect('/')
    else:
        form = JournalForm(1)
    context = {
        'form': form,
        'events': events,
        'goals': goals,
    }
    return render(request, 'morning.html', context)


def evening(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('-date')
    goals = GoalCategory.objects.all()
    if request.method == 'POST':
        form = JournalForm(2, request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect('/')
    else:
        form = JournalForm(2)
    context = {
        'form': form,
        'events': events,
        'goals': goals,
    }
    return render(request, 'morning.html', context)


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

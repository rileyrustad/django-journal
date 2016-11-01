from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .forms import MorningForm, EveningForm, GoalForm, EventForm
from .models import GoalCategory, Goal, Event



def index(request):
    return render(request, 'index.html')


def morning(request):
    goals = GoalCategory.objects.all()
    events = Event.objects.filter(date__gte=timezone.now()).order_by('-date')

    if request.method == 'POST':
        form = MorningForm(request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect('/')
    else:
        morning_form = MorningForm()
    context = {
        'morning_form': morning_form,
        'goals': goals,
        'events': events,
    }
    return render(request, 'morning.html', context)


def evening(request):
    if request.method == 'POST':
        form = EveningForm(request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect('/')
    else:
        form = EveningForm()

    return render(request, 'evening.html', {'form': form})


def goals(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['new_goal_text']
            category = form.cleaned_data['category']
            g = Goal(text=text, category=category)
            g.save()
            return HttpResponseRedirect('/')
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
            return HttpResponseRedirect('/')
    else:
        form = EventForm()

    return render(request, 'events.html', {'form': form})

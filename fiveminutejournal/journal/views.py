from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import MorningForm, EveningForm, GoalForm
from .models import GoalCategory, Goal


def index(request):
    return render(request, 'index.html')


def morning(request):
    goals = GoalCategory.objects.all()
    if request.method == 'POST':
        form = MorningForm(request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect('/')
    else:
        morning_form = MorningForm()

    return render(request, 'morning.html', {'morning_form': morning_form, 'goals':goals})


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
            g = Goal(text=text,category=category)
            g.save()
            return HttpResponseRedirect('/')
    else:
        form = GoalForm()

    return render(request, 'goals.html', {'form': form})
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import MorningForm, EveningForm


def index(request):
    return render(request, 'index.html')


def morning(request):
    if request.method == 'POST':
        form = MorningForm(request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect('/')
    else:
        form = MorningForm()

    return render(request, 'morning.html', {'form': form})

def evening(request):
    if request.method == 'POST':
        form = EveningForm(request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect('/')
    else:
        form = EveningForm()

    return render(request, 'evening.html', {'form': form})

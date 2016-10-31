from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import MorningForm


def index(request):
    return HttpResponse("Hello, world. You're at journal index.")

def morning(request):
    if request.method == 'POST':
        form = MorningForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save(True)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MorningForm()

    return render(request, 'morning.html', {'form': form})
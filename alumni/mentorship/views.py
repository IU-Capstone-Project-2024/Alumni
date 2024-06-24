# mentorship/views.py

from django.shortcuts import render

def intro(request):
    return render(request, 'mentorship/intro.html')

def form(request):
    return render(request, 'mentorship/form.html')

def thank_you(request):
    return render(request, 'mentorship/thank_you.html')

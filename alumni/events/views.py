from django.shortcuts import render
from .models import Events
from login.models import Interest
from django.db.models import Count
from django.db.models import Q

# Create your views here.

def page(request):
    countries = Events.objects.values_list('country', flat=True).distinct().order_by('country')
    cities = Events.objects.values_list('city', flat=True).distinct().order_by('city')
    tags = Interest.objects.values_list('name', flat=True).order_by('name')
    events = Events.objects.all()

    context = {
        'countries': countries,
        'cities': cities,
        'tags': tags,
        'events': events,
    }

    return render(request, 'events/events.html', context)

def filter_events(request):
    country = request.GET.get('country', '')
    city = request.GET.get('city', '')
    tags = request.GET.getlist('tags')

    events = Events.objects.all()

    if country:
        events = events.filter(country=country)
    if city:
        events = events.filter(city=city)
    if tags:
        q_objects = Q()
        for tag in tags:
            q_objects |= Q(tags__name=tag)

        events = events.filter(q_objects).distinct()

    return render(request, 'events/events.html', {'events': events})
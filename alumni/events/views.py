from django.shortcuts import render, get_object_or_404
from .models import Events
from login.models import Interest
from django.db.models import Count
from django.db.models import Q
from .services import get_recommended_events

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

def ai_recommendation(request):
    events = Events.objects.all()
    ids = get_recommended_events() # add arguments if needed
    events = events.filter(id__in=ids)

    return render(request, 'events/events.html', {'events': events})

def event_detail(request, event_link):
    event = get_object_or_404(Events, link=f"/events/{event_link}")
    return render(request, 'events/event_detail.html', {'event': event})
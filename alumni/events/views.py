from django.shortcuts import render, get_object_or_404
from .models import Events
from login.models import Interest, CustomUser
from django.db.models import Count
from django.db.models import Case, When
from django.db.models import Q
from .services import get_recommended_events
from my_profile.services import get_user_interests, add_user_activity, delete_user_activity
from django.http import JsonResponse
import json

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
    user = request.user
    if user.is_authenticated:
        interests = get_user_interests(user.email)
        events_list = []
        for event in events:
            event_tags = list(event.tags.values_list('name', flat=True))
            events_list.append([event.id, event_tags])

        ids = get_recommended_events(events_list, interests)
        preserved_order = Case(*[When(id=id, then=pos) for pos, id in enumerate(ids)])
        events = events.filter(id__in=ids).order_by(preserved_order)
    return render(request, 'events/events.html', {'events': events})

def event_detail(request, event_link):
    event = get_object_or_404(Events, link=f"/events/{event_link}")
    return render(request, 'events/event_detail.html', {'event': event})

def create_activity(request, action):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_link = data.get('event_link')
        event = get_object_or_404(Events, link=event_link)
        event_url = request.build_absolute_uri(event_link)

        user = request.user
        activity = f"<a href='{event_url}'>{event.event_name}</a><br>"

        if user.is_authenticated:
            user_email = user.email
            add_user_activity(user_email, activity) if action == 'add' else delete_user_activity(user_email, activity)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'User is not authenticated.'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def add_activity(request):
    return create_activity(request, action='add')

def delete_activity(request):
    return create_activity(request, action='delete')

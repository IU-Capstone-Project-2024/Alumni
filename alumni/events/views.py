from django.shortcuts import render
from .models import Events

# Create your views here.

def page(request):
    countries = Events.objects.values_list('country', flat=True).distinct().order_by('country')
    cities = Events.objects.values_list('city', flat=True).distinct().order_by('city')
    events = Events.objects.all()

    context = {
        'countries': countries,
        'cities': cities,
        'events': events,
    }

    return render(request, 'events/events.html', context)
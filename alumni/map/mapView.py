from django.shortcuts import render
from .models import CustomUser
from django.core.serializers import serialize
import json

def map_view(request):
    users = CustomUser.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
    users_data = [
        {
            'username': f"{user.first_name} {user.last_name}",
            'latitude': user.latitude,
            'longitude': user.longitude,
            'city': user.city,
            'country': user.country
        }
        for user in users
    ]
    return render(request, 'map.html', {'profiles_json': json.dumps(users_data)})

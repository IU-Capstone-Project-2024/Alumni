# # In map/views.py
# from django.shortcuts import render
# from .models import CustomUser  # Adjust the import based on your actual models.py location
# from geopy.geocoders import Nominatim
# import json

# def map_view(request):
#     users = CustomUser.objects.all()
#     geolocator = Nominatim(user_agent="alumni_site")
#     profiles = []

#     for user in users:
#         if user.city and user.country:
#             location = f"{user.city}, {user.country}"
#             loc = geolocator.geocode(location)
#             if loc:
#                 profiles.append({
#                     'username': f"{user.first_name} {user.last_name}",
#                     'latitude': loc.latitude,
#                     'longitude': loc.longitude
#                 })

#     context = {
#         'profiles_json': json.dumps(profiles)
#     }
#     return render(request, 'map.html', context)

# map/views.py

# map/views.py
import folium
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from .utils import get_all_users

def map_view(request):
    try:
        # Get users with their coordinates
        users = get_all_users()
        map_center = [20, 0]
        alumni_map = folium.Map(location=map_center, zoom_start=2)

        for user in users:
            coordinates = [user['latitude'], user['longitude']]
            folium.Marker(
                location=coordinates,
                popup=f"{user['alias']}"
            ).add_to(alumni_map)

        map_html = alumni_map._repr_html_()
        context = {'map_html': map_html}
        return render(request, 'map/map.html', context)
    except TemplateDoesNotExist as e:
        print(f"Template not found: {e}")
        raise e
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

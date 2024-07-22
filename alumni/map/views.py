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
            print(coordinates, user['email'])
            folium.Marker(
                location=coordinates,
                popup=f"{user['email']}"
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

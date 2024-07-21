from geopy.geocoders import Nominatim
from login.models import CustomUser

def get_all_users():
    geolocator = Nominatim(user_agent="myGeocoder")
    users_for_map = []

    for user in CustomUser.objects.all():
        location = geolocator.geocode(user.city)
        if location:
            user_data = {
                'alias': user.alias,
                'latitude': location.latitude,
                'longitude': location.longitude
            }
            users_for_map.append(user_data)
    
    return users_for_map

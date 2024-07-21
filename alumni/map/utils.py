# # map/utils.py
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderUnavailable
# from login.models import CustomUser

# def get_all_users():
#     geolocator = Nominatim(user_agent="myGeocoder")
#     users_for_map = []

#     for user in CustomUser.objects.all():
#         try:
#             location = geolocator.geocode(user.location)
#             if location:
#                 user_data = {
#                     'email': user.alias,
#                     'latitude': location.latitude,
#                     'longitude': location.longitude
#                 }
#                 users_for_map.append(user_data)
#         except GeocoderUnavailable as e:
#             print(f"Geocoding service is unavailable: {e}")

#     return users_for_map

# map/utils.py





# map/utils.py
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderUnavailable, GeocoderInsufficientPrivileges, GeocoderTimedOut
# import time
# from login.models import CustomUser

# def get_all_users():
#     geolocator = Nominatim(user_agent="myGeocoder")
#     users_for_map = []

#     def geocode_with_retry(query, retries=3, delay=2):
#         for attempt in range(retries):
#             try:
#                 return geolocator.geocode(query)
#             except GeocoderTimedOut:
#                 if attempt < retries - 1:
#                     time.sleep(delay)
#                     delay *= 2  # Exponential backoff
#                 else:
#                     raise
#             except GeocoderUnavailable as e:
#                 print(f"Geocoding service is unavailable: {e}")
#                 raise
#             except GeocoderInsufficientPrivileges as e:
#                 print(f"Insufficient privileges: {e}")
#                 raise

#     # Check the user data directly
#     for user in CustomUser.objects.all():
#         print(f"User: {user.email}, Location: {user.location}")

#         try:
#             print(f'trying to convert location for user {user.email}')
#             location = geocode_with_retry(user.location)
#             if location:
#                 user_data = {
#                     'email': user.email,
#                     'latitude': location.latitude,
#                     'longitude': location.longitude
#                 }
#                 print(f'user: {user.email}, loc: {user.location}, lat: {location.latitude}, lat: {location.longitude}')
#                 users_for_map.append(user_data)
#         except (GeocoderUnavailable, GeocoderInsufficientPrivileges, GeocoderTimedOut) as e:
#             print(f"Error geocoding user {user.alias}: {e}")
#             # Optionally add fallback data or handle errors as needed

#     return users_for_map

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderInsufficientPrivileges, GeocoderTimedOut
import time
from login.models import CustomUser

def geocode_with_retry(geolocator, query, retries=3, delay=2, timeout=10):
    for attempt in range(retries):
        try:
            return geolocator.geocode(query, timeout=timeout)
        except GeocoderTimedOut:
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise
        except GeocoderUnavailable as e:
            print(f"Geocoding service is unavailable: {e}")
            raise
        except GeocoderInsufficientPrivileges as e:
            print(f"Insufficient privileges: {e}")
            raise

def get_all_users():
    geolocator = Nominatim(user_agent="myGeocoder")
    users_for_map = []

    # Check the user data directly
    for user in CustomUser.objects.all():
        print(f"User: {user.email}, Location: {user.location}")

        try:
            print(f'Trying to convert location for user {user.email}')
            location = geocode_with_retry(geolocator, user.location)
            if location:
                user_data = {
                    'email': user.email,
                    'latitude': location.latitude,
                    'longitude': location.longitude
                }
                print(f'User: {user.email}, Loc: {user.location}, Lat: {location.latitude}, Lon: {location.longitude}')
                users_for_map.append(user_data)
        except (GeocoderUnavailable, GeocoderInsufficientPrivileges, GeocoderTimedOut) as e:
            print(f"Error geocoding user {user.email}: {e}")
            # Optionally add fallback data or handle errors as needed

    return users_for_map

import requests
import time
from login.models import CustomUser

def geocode_with_retry(query, api_key, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(
                "https://us1.locationiq.com/v1/search.php",
                params={
                    "key": api_key,
                    "q": query,
                    "format": "json"
                },
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data[0]  # Return the first result
            else:
                print(f"Geocoding service returned status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Geocoding request error: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise
    return None

def get_all_users():
    api_key = "pk.278bdae7719c5290604d333b3c274721"  # Replace with your LocationIQ API key
    users_for_map = []

    for user in CustomUser.objects.all():
        print(f"User: {user.email}, Location: {user.location}")

        try:
            print(f'Trying to convert location for user {user.email}')
            location = geocode_with_retry(user.location, api_key)
            if location:
                user_data = {
                    'email': user.email,
                    'latitude': float(location['lat']),
                    'longitude': float(location['lon'])
                }
                print(f'User: {user.email}, Loc: {user.location}, Lat: {location["lat"]}, Lon: {location["lon"]}')
                users_for_map.append(user_data)
        except Exception as e:
            print(f"Error geocoding user {user.email}: {e}")
            # Optionally add fallback data or handle errors as needed

    return users_for_map

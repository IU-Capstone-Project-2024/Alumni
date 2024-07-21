from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.utils.safestring import mark_safe

# Define the pages and their hyperlinks
pages = ["Card request", "Market", "My profile", "Mentorship", "Donation", "Events", "Map"]
hyperlinks = {
    'Card request': '<a href="http://130.193.43.164/card_request/" style="color: blue;" target="_blank">Card request</a>',
    'Market': '<a href="http://130.193.43.164/market/" style="color: blue;" target="_blank">Market</a>',
    'My profile': '<a href="http://130.193.43.164/my_profile/profile/" style="color: blue;" target="_blank">My profile</a>',
    'Mentorship': '<a href="http://130.193.43.164/mentorship/" style="color: blue;" target="_blank">Mentorship</a>',
    'Donation': '<a href="http://130.193.43.164/donation/" style="color: blue;" target="_blank">Donation</a>',
    'Events': '<a href="https://130.193.43.164/events/" style="color: blue;" target="_blank">Events</a>',
    'Map': '<a href="https://130.193.43.164/map/" style="color: blue;" target="_blank">Map</a>'
}

# Preprocess the text input
def preprocess_text(text):
    return text.lower().strip()

# Check for inappropriate content
def contains_inappropriate_content(text):
    inappropriate_words = ['sex', 'death', 'violence', 'drugs', 'abuse', 'depression']
    return any(word in text.lower() for word in inappropriate_words)

# Create hyperlinks for responses
def create_hyperlinks(page):
    return mark_safe(hyperlinks.get(page, ''))

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')
        options = ["Card request", "Market", "My profile", "Mentorship", "Donation", "Events", "Homepage", "Map"]
        options.sort()
        search_query = preprocess_text(message)

        if contains_inappropriate_content(search_query):
            response = "I didn't understand you. We have options:\n" + ", ".join(options)
        else:
            # Select a random page
            random_page = random.choice(pages)
            response = create_hyperlinks(random_page)

        return JsonResponse({'response': str(response)})

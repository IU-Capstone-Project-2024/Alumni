from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from django.utils.safestring import mark_safe
import requests

# Define Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer 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"}

pages = ["Card request", "Hello! How can I help you?", "Market",
         "My profile", "Mentorship", "Donation", "Events", "Map"]

# Define webpages and their descriptions
webpages = [
    "Request a card for access. card. Pass. Enter. Arrive. Go. University. Innopolis. Запрос карты для доступа. карта. Пропуск. Войти. Прибыть. Идти. Университет. Иннополис.",
    "Say hello. Hi. Hello. Good afternoon. Good evening. Good night. Hey. Скажите привет. Привет. Добрый день. Добрый вечер. Доброй ночи. Привет.",
    "Shop for merchandise. Shop. Inno Shop. Merch. Merchandise. Gift. Магазин для покупок. Магазин. Ино Магазин. Товары. Подарок.",
    "Log in to your profile. Profile. Authorization. User. Войти в профиль. Профиль. Авторизация. Пользователь.",
    "Get support from mentors. Students. Teacher. Mentors. Mentorship. Support. Получить поддержку от наставников. Ментор. Студенты. Учитель. Наставники. Наставничество. Поддержка.",
    "Make a donation. Donation. Money. Gifting. Gift. Supporting. Сделать пожертвование. Пожертвование. Деньги. Подарок. Поддержка.",
    "Learn about events. Meetups. Conferences. Events. Clubs. Узнать о событиях. Встречи. Конференции. События. Клубы.",
    "Find locations on the map. Map. Alumnus. Cities. World. Найти местоположения на карте. Карта. Выпускник. Города. Мир."
]

webpage_keys = pages
webpage_descriptions = webpages

# Function to call Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Preprocess the text input
def preprocess_text(text):
    return text.lower().strip()

# Check for inappropriate content
def contains_inappropriate_content(text):
    inappropriate_words = ['sex', 'death', 'violence', 'drugs', 'abuse', 'depression']
    return any(word in text.lower() for word in inappropriate_words)

# Create hyperlinks for responses
def create_hyperlinks(text):
    hyperlinks = {
        'Card request': '<a href="http://130.193.43.164/card_request/" style="color: blue;" target="_blank">Card request</a>',
        'Market': '<a href="http://130.193.43.164/market/" style="color: blue;" target="_blank">Market</a>',
        'My profile': '<a href="http://130.193.43.164/my_profile/profile/" style="color: blue;" target="_blank">My profile</a>',
        'Mentorship': '<a href="http://130.193.43.164/mentorship/" style="color: blue;" target="_blank">Mentorship</a>',
        'Donation': '<a href="http://130.193.43.164/donation/" style="color: blue;" target="_blank">Donation</a>',
        'Events': '<a href="https://130.193.43.164/events/" style="color: blue;" target="_blank">Events</a>',
        'Map': '<a href="https://130.193.43.164/map/" style="color: blue;" target="_blank">Map</a>'
    }

    for key, link in hyperlinks.items():
        if key in text:
            text = text.replace(key, link)
            break      
    return mark_safe(text)

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
            similarity_embedding = query({
                "inputs": {
                    "source_sentence": search_query,
                    "sentences": webpages,
                },
            })

            print("   ", similarity_embedding)

            # Find the index of the highest similarity score
            most_similar_idx = np.argmax(similarity_embedding)

            # Get the most similar webpage description
            most_similar_webpage = webpage_keys[most_similar_idx]


            print(f"Query: {search_query}, Most Similar Webpage: {most_similar_webpage}")
            # if score_text < 0.25:
            #     response = "I didn't understand you. We have options:\n" + "\n".join(options)
            # else:
            #     response = create_hyperlinks(most_similar_webpage.replace('_', ' '))
            response = create_hyperlinks(most_similar_webpage.replace('_', ' '))

        return JsonResponse({'response': str(response)})

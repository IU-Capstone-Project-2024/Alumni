from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util
from django.utils.safestring import mark_safe

# Initialize Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Define webpages and their descriptions
webpages = {
    "Card request": "Request a card for access. card. Pass. Enter. Arrive. Go. University. Innopolis. Запрос карты для доступа. карта. Пропуск. Войти. Прибыть. Идти. Университет. Иннополис.",
    "Hello! How can I help you?": "Say hello. Hi. Hello. Good afternoon. Good evening. Good night. Hey. Скажите привет. Привет. Добрый день. Добрый вечер. Доброй ночи. Привет.",
    "Market": "Shop for merchandise. Shop. Inno Shop. Merch. Merchandise. Gift. Магазин для покупок. Магазин. Ино Магазин. Товары. Подарок.",
    "My profile": "Log in to your profile. Profile. Authorization. User. Войти в профиль. Профиль. Авторизация. Пользователь.",
    "Mentorship": "Get support from mentors. Students. Teacher. Mentors. Mentorship. Support. Получить поддержку от наставников. Ментор. Студенты. Учитель. Наставники. Наставничество. Поддержка.",
    "Donation": "Make a donation. Donation. Money. Gifting. Gift. Supporting. Сделать пожертвование. Пожертвование. Деньги. Подарок. Поддержка.",
    "Events": "Learn about events. Meetups. Conferences. Events. Clubs. Узнать о событиях. Встречи. Конференции. События. Клубы.",
    "Map": "Find locations on the map. Map. Alumnus. Cities. World. Найти местоположения на карте. Карта. Выпускник. Города. Мир."
}


webpage_keys = list(webpages.keys())
webpage_descriptions = list(webpages.values())

webpage_embeddings = model.encode(webpage_descriptions, convert_to_tensor=True)

def preprocess_text(text):
    return text.lower().strip()

def contains_inappropriate_content(text):
    inappropriate_words = ['sex', 'death', 'violence', 'drugs', 'abuse', 'depression']
    return any(word in text.lower() for word in inappropriate_words)

def create_hyperlinks(text):
    hyperlinks = {
        'Card request': '<a href="http://130.193.43.164/card_request/" style="color: blue;" target="_blank">Card request</a>',
        'Market': '<a href="http://130.193.43.164/market/" style="color: blue;" target="_blank">Market</a>',
        'My profile': '<a href="http://130.193.43.164/my_profile/profile/" style="color: blue;" target="_blank">My profile</a>',
        'Mentorship': '<a href="http://130.193.43.164/mentorship/" style="color: blue;" target="_blank">Mentorship</a>',
        'Donation': '<a href="http://130.193.43.164/donation/" style="color: blue;" target="_blank">Donation</a>',
        'Events': '<a href="https://130.193.43.164/events/" style="color: blue;" target="_blank">Events</a>',
        # 'Homepage': '<a href="https://130.193.43.164/main/" style="color: blue;" target="_blank">Homepage</a>',
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
            search_query_embedding = model.encode([search_query], convert_to_tensor=True)[0]
            cosine_similarities = util.pytorch_cos_sim(search_query_embedding, webpage_embeddings)[0].cpu().numpy()
            most_similar_idx = np.argmax(cosine_similarities)
            most_similar_webpage = webpage_keys[most_similar_idx]
            score_text = cosine_similarities[most_similar_idx]

            print(f"Query: {search_query}, Most Similar Webpage: {most_similar_webpage}, Score: {score_text}")

            if score_text < 0.25:
                response = "I didn't understand you. We have options:\n" + "\n".join(options)
            else:
                response = create_hyperlinks(most_similar_webpage.replace('_', ' '))

        return JsonResponse({'response': str(response)})

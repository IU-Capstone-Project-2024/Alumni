from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import nltk
import numpy as np
from sentence_transformers import SentenceTransformer, util
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin  # Import admin module

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize Sentence Transformer model
model = SentenceTransformer("sentence-transformers/distilbert-base-nli-stsb-mean-tokens")

# Define webpages and their descriptions
webpages = {
    "Card request": "Card request. Card. Pass. Enter. Arrive. Go. University. Innopolis.",
    "Hello! How can I help you?": "Hi. Hello. Good afternoon. Good evening. Good night. Hey.",
    "Market": "Shop. Inno Shop. Merch. Merchandize. Gift.",
    "My profile": "Log in. Profile. Authorization. User.",
    "Mentorship": "Students. Teacher. Mentors. Mentorship. Support",
    "Donation": "Donation. Money. Gifting. Gift. Supporting.",
    "Events": "Meetups. Conferences. Events. Clubs",
    "Homepage": "Homepage. Home. Menu.",
    "Map": "Map. Alumnus. Cities. World"
}

# Convert webpages dictionary into lists for further processing
webpage_keys = list(webpages.keys())
webpage_descriptions = list(webpages.values())

# Encode webpage descriptions using Sentence Transformer model
webpage_embeddings = model.encode(webpage_descriptions, convert_to_tensor=True)

# Function to preprocess text (lowercase and strip)
def preprocess_text(text):
    text = text.lower().strip()
    return text

# Function to check for inappropriate content
def contains_inappropriate_content(text):
    inappropriate_words = ['sex', 'death', 'violence', 'drugs', 'abuse', 'depression']
    for word in inappropriate_words:
        if word in text.lower():
            return True
    return False

# Function to create hyperlinks
def create_hyperlinks(text):
    hyperlinks = {
        'Card request': '<a href="http://130.193.43.164/card_request/">Card request</a>',
        'Market': '<a href="http://130.193.43.164/market/">Market</a>',
        'My profile': '<a href="http://130.193.43.164/my_profile/profile/">My profile</a>',
        'Mentorship': '<a href="http://130.193.43.164/mentorship/">Mentorship</a>',
        'Donation': '<a href="http://130.193.43.164/donation/">Donation</a>',
        'Events': '<a href="https://130.193.43.164/events/">Events</a>',
        'Homepage': '<a href="https://130.193.43.164/main/">Homepage</a>',
        'Map': '<a href="https://130.193.43.164/map/">Map</a>'
    }
    
    for key, link in hyperlinks.items():
        text = text.replace(key, link)
    return text

# CSRF exempted view for handling chat requests
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')
        options = ["Card request", "Market", "My profile", "Mentorship", "Donation", "Events", "Homepage", "Map"]
        options.sort()
        search_query = preprocess_text(message)

        if contains_inappropriate_content(search_query):
            response = "I didn't understand you. We have options:\n" + "\n".join(options)
        else:
            search_query_embedding = model.encode([search_query], convert_to_tensor=True)[0]
            cosine_similarities = util.pytorch_cos_sim(search_query_embedding, webpage_embeddings)[0].cpu().numpy()
            most_similar_idx = np.argmax(cosine_similarities)
            most_similar_webpage = webpage_keys[most_similar_idx]
            score_text = cosine_similarities[most_similar_idx]

            # Print the score to the console
            print(f"Query: {search_query}, Most Similar Webpage: {most_similar_webpage}, Score: {score_text}")

            if score_text < 0.2:
                response = "I didn't understand you. We have options:\n" + "\n".join(options)
            else:
                response = create_hyperlinks(most_similar_webpage.replace('_', ' '))

        return JsonResponse({'response': response})

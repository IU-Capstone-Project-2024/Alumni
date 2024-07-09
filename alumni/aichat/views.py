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
    "card_request/": "Card request. Pass. Enter. Arrive. Go. University. Innopolis.",
    "market/": "Shop. Inno Shop. Merch. Merchandize. Gift.",
    "my_profile/": "Log in. Profile. Authorization. User.",
    "Mentorship": "Students. Teacher. Mentors. Mentorship. Support",
    "Authors": "Authors.",
    "donation/": "Donation. Money. Gifting. Gift. Supporting.",
    "Events": "Meetups. Conferences. Events. Clubs",
    "main/": "Homepage. Home. Menu.",
    "Map": "Map. Alumnus. Cities. World"
}

# Define Django URL patterns
urlpatterns = [
    path("", include("login.urls")),
    path('admin/', admin.site.urls),  # Add admin URL pattern
    path('main/', include("main.urls")),
    path("market/", include("market.urls")),
    path("my_profile/", include("my_profile.urls")),
    path("card_request/", include("card_request.urls")),
    path("donation/", include("donation.urls")),
    path('', include('aichat.urls')),
]

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

# CSRF exempted view for handling chat requests
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')

        search_query = preprocess_text(message)

        if contains_inappropriate_content(search_query):
            response = "I didn't understand you. Please revise your query."
        else:
            search_query_embedding = model.encode([search_query], convert_to_tensor=True)[0]
            cosine_similarities = util.pytorch_cos_sim(search_query_embedding, webpage_embeddings)[0].cpu().numpy()
            most_similar_idx = np.argmax(cosine_similarities)
            most_similar_webpage = webpage_keys[most_similar_idx]
            score_text = cosine_similarities[most_similar_idx]

            if score_text < 0.1:
                response = "I didn't understand you. Please revise your query."
            else:
                response = most_similar_webpage.replace('_', ' ')

        return JsonResponse({'response': response})

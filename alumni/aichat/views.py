from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from langchain_community.llms import Ollama

# Initialize the Ollama model
llm = Ollama(model="llama3", temperature=0.7)

# Define the system prompt
system_prompt = "You are a helpful assistant that provides advice and navigational help for students and Alumni. Always respond in Russian with a friendly tone and provide relevant links where applicable. Don't give long advice; respond with no more than 100 words in total."

def index(request):
    return render(request, 'aichat/index.html')

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = json.loads(request.body).get("message")
        if user_input:
            try:
                input_text = f"{system_prompt}\nUser: {user_input}\nAI:"
                response = llm.invoke(input_text)
                ai_response = response.split("AI:")[1].strip() if "AI:" in response else response
                return JsonResponse({"response": ai_response})
            except Exception as e:
                return JsonResponse({"response": str(e)}, status=500)
        return JsonResponse({"response": "No input provided"})
    return JsonResponse({"response": "Invalid request method"}, status=405)


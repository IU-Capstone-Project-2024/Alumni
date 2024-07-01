from datetime import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Alumni
from django.http import JsonResponse

# Create your views here.

def page(request):
    return render(request, 'card_request/card_request.html')

def handle_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email').lower()
        telegram = request.POST.get('telegram')
        visit_date = datetime.strptime(request.POST.get('visit-date'), '%Y-%m-%d').date()
        if Alumni.objects.filter(email=email).exists():
            visit_date_str = visit_date.strftime('%d.%m.%Y')
            send_mail(
                'Alumni - University Visit Request',
                f'Name: {name}\n'
                f'Surname: {surname}\n'
                f'Email: {email}\n'
                f'Telegram: {telegram}\n'
                f'Visit Date: {visit_date_str}\n',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_TO],
                fail_silently=False,
            )

    return JsonResponse({'message': 'Success'}, status=200)

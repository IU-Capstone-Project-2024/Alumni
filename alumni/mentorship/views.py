from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def intro(request):
    return render(request, 'mentorship/intro.html')

def form(request):
    print(request.method)
    if request.method == 'POST':
        print("Method is post")
        about_you = request.POST.get('about-you')
        availability = request.POST.get('availability')
        motivation = request.POST.get('motivation')
        telegram_alias = request.POST.get('telegram-alias')
        mentorship_type = request.POST.get('mentorship-type')
        send_mail(
                'Alumni - Mentorship Form',
                f'About mentor: {about_you}\n'
                f'Availability: {availability}\n'
                f'Motivation: {motivation}\n'
                f'Telegram: {telegram_alias}\n'
                f'Mentorship type: {mentorship_type}\n',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_TO],
                fail_silently=False,
            )
        return redirect('thank_you')
        
    return render(request, 'mentorship/form.html')

def thank_you(request):
    return render(request, 'mentorship/thank_you.html')

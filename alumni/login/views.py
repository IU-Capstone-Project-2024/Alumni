from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user, username, password)
            auth_login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login/login.html', {'error': 'Invalid email or password'})
    return render(request, 'login/login.html')
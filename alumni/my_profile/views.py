from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.models import CustomUser
from .forms import ProfileForm

@login_required
def profile_view(request):
    try:
        user_profile = request.user
    except CustomUser.DoesNotExist:
        user_profile = None
    
    return render(request, 'my_profile/profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    user_profile = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user_profile.save()
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'my_profile/edit_profile.html', {'form': form, 'user_profile': user_profile})
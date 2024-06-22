from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def profile_view(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = None
    
    return render(request, 'my_profile/profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user, defaults={
            'graduation_year': 2015,  
            'position': '-',   
            'company': '-',
            'location': '-'
        })
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    
    return render(request, 'my_profile/edit_profile.html', {'form': form})
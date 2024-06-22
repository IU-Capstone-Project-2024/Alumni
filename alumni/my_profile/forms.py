from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'graduation_year',
            'position',
            'company',
            'location',
            'interests',
            'activities'
        ]
        widgets = {
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'interests': forms.Textarea(attrs={'class': 'form-control'}),
            'activities': forms.Textarea(attrs={'class': 'form-control'}),
        }

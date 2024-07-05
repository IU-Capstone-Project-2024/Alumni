from django import forms
from login.models import CustomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'user_photo',
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

    user_photo = forms.ImageField(required=False)
    graduation_year = forms.IntegerField(required=False)
    position = forms.CharField(required=False)
    company = forms.CharField(required=False)
    location = forms.CharField(required=False)
    interests = forms.CharField(widget=forms.Textarea, required=False)
    activities = forms.CharField(widget=forms.Textarea, required=False)

    
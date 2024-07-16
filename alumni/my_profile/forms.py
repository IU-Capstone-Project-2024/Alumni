from django import forms
from django_select2.forms import Select2TagWidget
from login.models import CustomUser, Interest

class ProfileForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class' : 'select2'}),
        required=False
    )
    class Meta:
        model = CustomUser
        fields = [
            'user_photo',
            'alias',
            'graduation_year',
            'position',
            'company',
            'location',
            'interests',
        ]
        widgets = {
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'interests': Select2TagWidget(attrs={'class': 'form-control'}),
        }

    user_photo = forms.ImageField(required=False)
    graduation_year = forms.IntegerField(required=False)
    position = forms.CharField(required=False)
    company = forms.CharField(required=False)
    location = forms.CharField(required=False)
    activities = forms.CharField(widget=forms.Textarea, required=False)

    
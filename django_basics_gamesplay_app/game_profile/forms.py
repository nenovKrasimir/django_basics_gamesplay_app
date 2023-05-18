from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'email': forms.EmailField(attrs={'placeholder': 'Email'}),
            'age': forms.IntegerField(),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'first_name': forms.CharField(attrs={'placeholder': 'First Name'}),
            'last_name': forms.CharField(attrs={'placeholder': 'Last Name'}),
            'profile_picture': forms.URLField()
        }
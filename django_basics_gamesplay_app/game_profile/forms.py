from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),}
        #     'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        #     'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        #     'profile_picture': forms.URLInput(attrs={'placeholder': 'Image url'})
        # }

        labels = {
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',}
        #     'first_name': 'First Name',
        #     'last_name': 'Last Name',
        #     'profile_picture': 'Profile Picture',
        # }
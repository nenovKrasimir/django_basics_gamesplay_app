from django import forms
from .models import Game


class GameFrom(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        widgets = {
            'title': forms.CharField(attrs={'placeholder': 'Title'}),
            'category': forms.CharField(attrs={'placeholder': 'Category'}),
            'rating': forms.FloatField(),
            'max_level': forms.IntegerField(),
            'image_url': forms.URLField(),
            'summary': forms.TextInput(attrs={'placeholder': 'Summary'})
        }
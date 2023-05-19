from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        category = forms.ChoiceField(choices=Game.CHOICES)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'rating': forms.NumberInput(),
            'max_level': forms.NumberInput(),
            'image_url': forms.URLInput(),
            'summary': forms.Textarea(attrs={'placeholder': 'Summary'})
        }
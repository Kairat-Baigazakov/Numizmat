from django import forms
from .models import CoinObj


class CoinForm(forms.ModelForm):

    class Meta:
        model = CoinObj
        fields = ('title.title', 'title.description', 'type.title', 'theme.title', 'nominal', 'diameter', 'weight')

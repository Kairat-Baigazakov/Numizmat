from django import forms
from .models import CoinObj


class CoinForm(forms.ModelForm):

    class Meta:
        model = CoinObj
        fields = ('title', 'type', 'theme', 'nominal', 'diameter', 'weight')

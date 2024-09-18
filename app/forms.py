from django import forms
from .models import CoinObj, Coin, Theme, Type


class Type(forms.ModelForm):
    class Meta:
        model = Type
        fields = ('title', 'proba', 'technology')


class Theme(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('title')


class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ('title', 'description')


class CoinObjForm(forms.ModelForm):
    class Meta:
       model = CoinObj
       fields = ('title', 'type', 'theme', 'nominal', 'diameter', 'weight')

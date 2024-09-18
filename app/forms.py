from django import forms
from .models import CoinObj


class CoinForm(forms.ModelForm):

    title = forms.CharField(max_length=60)
    description = forms.CharField(max_length=100)
    type = forms.CharField(max_length=30)
    proba = forms.IntegerField()
    technology = forms.CharField(max_length=50)
    theme = forms.CharField(max_length=30)
    nominal = forms.IntegerField()
    weight = forms.IntegerField()
    diameter = forms.IntegerField()
    #class Meta:
    #    model = CoinObj
    #    fields = ('title', 'type', 'theme', 'nominal', 'diameter', 'weight')

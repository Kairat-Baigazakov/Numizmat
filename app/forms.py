from django import forms
from .models import CoinObj


class CoinForm(forms.ModelForm):

    title = forms.CharField(max_length=60)
    description = forms.TextField()
    type = forms.CharField(max_length=30)
    proba = forms.PositiveIntegerField()
    technology = forms.CharField(max_length=50)
    theme = forms.CharField(max_length=30)
    nominal = forms.PositiveSmallIntegerField()
    weight = forms.FloatField()
    diameter = forms.FloatField()
    #class Meta:
    #    model = CoinObj
    #    fields = ('title', 'type', 'theme', 'nominal', 'diameter', 'weight')

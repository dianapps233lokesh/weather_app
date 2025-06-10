from django import forms

from .models import WeatherModel

class WeatherForm(forms.ModelForm):
    class Meta:
        model=WeatherModel
        fields="__all__"
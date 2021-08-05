from django import forms
from django.forms import fields
from .models import FeedBack, Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'description']

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['place', 'text']
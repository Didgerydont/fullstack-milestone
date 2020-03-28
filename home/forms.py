from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import ItemRequest


class RequestItemForm(forms.ModelForm):
    name = forms.CharField(max_length=254, required=True)
    description = forms.CharField(max_length=999, required=True, widget=forms.Textarea)
    budget = forms.IntegerField(required=True)
    image = forms.ImageField(required=True)
    contact = forms.EmailField(required=True)

    class Meta:
        model = ItemRequest
        fields = ['name', 'description', 'budget', 'image', 'contact']

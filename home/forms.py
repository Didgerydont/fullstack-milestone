from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import ItemRequest


class RequestItemForm(forms.ModelForm):

    class Meta:
        model = ItemRequest
        fields = ['name', 'description', 'budget', 'image', 'contact']

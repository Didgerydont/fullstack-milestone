from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import ItemRequest


class RequestItemForm(forms.ModelForm):
    name = forms.CharField(max_length=254, default='')
    description = forms.TextField()
    budget = forms.IntegerField()
    image = forms.ImageField(upload_to='images')
    request_date = forms.DateTimeField(auto_now_add=True)
    contact = forms.EmailField(default='', required=True)

    class Meta:
        model = ItemRequest
        fields = ['name', 'description', 'budget', 'image']
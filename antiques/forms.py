from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from . import models
from .models import Enquire
from django.core.exceptions import ValidationError

class EnquiryForm(forms.ModelForm):
    enquiry = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Enquire
        fields = ['enquiry']
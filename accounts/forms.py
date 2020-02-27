from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserDetails
from phone_field import PhoneField


class UserLoginForm(forms.Form):
    """ Form to be used to log users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """ Form used to register a new user """
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2

class UserProfileForm(forms.Form):
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = forms.CharField(max_length=255, required=True)
    town = forms.CharField(max_length=45, required=True)
    post_code = forms.CharField(max_length=45, required=True)
    country = forms.CharField(max_length=45, required=True)

    class Meta:
        model = UserDetails
        fields = ['firstname', 'lastname', 'phone', 'address', 'town', 
                  'post_code', 'country']

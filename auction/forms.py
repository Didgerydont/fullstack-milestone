from django import forms
from .models import Bid
from antiques.models import Antiques


class BidForm(forms.ModelForm):
    """ Form to outbid previous offer """

    class Meta:
        model = Bid
        fields = ['new_bid']

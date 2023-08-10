from django import forms
from .models import AuctionableModel
class NewAuctionablesForm(forms.ModelForm):
    class Meta:
        model = AuctionableModel 
        fields = ('item_name','item_price_bid','item_highest_price','item_quatity')


class UpdateAuctionableForm(forms.ModelForm):
    class Meta:
        model = AuctionableModel
        fields =  fields = ('item_name','item_price_bid','item_quatity') 
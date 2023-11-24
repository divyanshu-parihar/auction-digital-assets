from django import forms
from .models import AuctionableModel,AuctionableBids
class NewAuctionablesForm(forms.ModelForm):
    class Meta:
        model = AuctionableModel 
        fields = ('item_name','item_price_bid','item_highest_price','item_quatity','item_image')


class UpdateAuctionableForm(forms.ModelForm):
    class Meta:
        model = AuctionableModel
        fields = ('item_name','item_price_bid','item_quatity','item_image') 


class AuctionBiddingForm(forms.ModelForm):
    class Meta:
        model = AuctionableBids
        fields = ('item_owner','item_bid_amount','bidder_email','item_description')
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuctionableModel(models.Model):
    item_owner = models.ForeignKey(to=User,to_field='username',on_delete=models.CASCADE,default=1)
    item_name = models.CharField(primary_key = True,max_length=1000,blank=False,unique=True)
    item_price_bid = models.IntegerField()
    item_highest_price= models.IntegerField()
    item_quatity = models.IntegerField()
    item_image = models.TextField()
    def __str__(self):
        return self.item_name + "(" + self.item_owner.username + ")"
    
class AuctionableBids(models.Model):
    item_owner = models.ForeignKey(to=User, to_field='username', on_delete=models.CASCADE)
    item_bid_amount = models.IntegerField()
    bidder_email = models.EmailField()
    item_description = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.bidder_email
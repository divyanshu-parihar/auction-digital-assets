from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuctionableModel(models.Model):
    item_owner = models.ForeignKey(to=User,to_field='username',on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=1000,blank=False)
    item_price_bid = models.IntegerField()
    item_highest_price= models.IntegerField()
    item_quatity = models.IntegerField()

    def __str__(self):
        return self.item_name + "(" + self.item_owner.username + ")"
    

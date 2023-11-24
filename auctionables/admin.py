from django.contrib import admin
from .models import AuctionableModel,AuctionableBids
# Register your models here.
admin.site.register(AuctionableModel)
admin.site.register(AuctionableBids)
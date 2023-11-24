
from django.urls import path
from .views import new_item,me_items,update_item,del_item,auction_domain

urlpatterns = [
    path('new/',new_item,name='item_new'),
    path('me/',me_items,name='item_list'),
    path('update/<int:idx>',update_item,name='item_update'),
    path('delete/<int:idx>',del_item),
    path('auction/',auction_domain,name = 'auction_domain')
]
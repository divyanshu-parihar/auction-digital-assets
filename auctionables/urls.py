
from django.urls import path
from .views import new_item,me_items,update_item,del_item

urlpatterns = [
    path('new/',new_item),
    path('me/',me_items,name='item_list'),
    path('update/<int:idx>',update_item),
    path('delete/<int:idx>',del_item)
]
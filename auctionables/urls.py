
from django.urls import path
from .views import new_item,me_items

urlpatterns = [
    path('new/',new_item),
    path('me/',me_items)
]

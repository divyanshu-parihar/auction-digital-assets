from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('',home),
    path('auth/',include('auth.urls'))
]

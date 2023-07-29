from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import home

urlpatterns = [
    path('',home),
    path('auth/',include('auth.urls')),
    path('accounts/',include('accounts.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html' ,authentication_form=LoginForm)),
    path('register/',register),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

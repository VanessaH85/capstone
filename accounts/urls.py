"""Account urls

Now, you want to create a login page for the user. Start by creating a templates/authentication/
login.html in the user_auth/ folder. Now, set up your user_login view in views.py to take the user
to the login page:"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
app_name = 'accounts'
urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('add_profile', views.add_profile, name='add-profile'),
]


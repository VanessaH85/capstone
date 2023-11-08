"""Urls for mysite project
Add a URL that will point to your app.
Append the urls so that they will point to your applications in urls.py"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('band.urls')),
    path('accounts/', include('accounts.urls')),

]

"""Django admin

Built-in, model-centric interface that allows trusted users to manage content on you site.
The admin interface reads metadata from your models to provide a quick, model-centric interface
where trusted users can manage content on your site."""

from django.contrib import admin
from .models import UserProfile, UserPersona, UserInterest

admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(UserInterest)



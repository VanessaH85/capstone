"""Accounts View

Contains the logic that governs the user's request and determines the appropriate response.
View doesn’t necessarily mean ‘display’.

Accounts View relates your Model and Template together through URLs.
The View component helps to determine which information data in your Model should be communicated via
your Template"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from .forms import ProfileForm


def add_profile(request: HttpRequest) -> HttpResponse:
    submitted = False
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/add_profile?submitted=True')
    else:
        form = ProfileForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'accounts/add_profile.html', {'form': form, 'submitted': submitted})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

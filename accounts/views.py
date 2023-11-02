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

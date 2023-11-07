""" My band views

View: contains the logic that governs the user’s request and determines the appropriate response.
View doesn’t necessarily mean ‘display’.

Band view relates your Model and Template together through URLs.
The View component helps to determine which information data in your Model should be communicated via
your Template"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index (request: HttpRequest) -> HttpResponse:
    return render(request, 'band/index.html')

def about (request: HttpRequest) -> HttpResponse:
    return render(request,'band/about.html')

def songs (request: HttpRequest) -> HttpResponse:
    return render(request,'band/songs.html')

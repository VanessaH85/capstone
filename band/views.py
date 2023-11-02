from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index (request: HttpRequest) -> HttpResponse:
    return render(request, 'band/index.html')

def about (request: HttpRequest) -> HttpResponse:
    return render(request,'band/about.html')

def songs (request: HttpRequest) -> HttpResponse:
    return render(request,'band/songs.html')

from django.urls import path

from . import views

app_name = 'band'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('songs', views.songs, name='songs'),
]

"""Django ModelForm is a class that is used to directly convert a model into a Django form. Because
you are building a database-driven app, the forms are map closely to Django models"""

from django import forms
from django.forms import ModelForm
from .models import UserProfile


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'is_full_name_displayed', 'bio', 'website', 'interests')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'is_full_name_displayed': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'interests': forms.TextInput(attrs={'class': 'form-control'}),
        }


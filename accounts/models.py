from django.db import models
"""Accounts Model

Refers to the reference source for the database fields and associated behaviour for the data you consume
in your application. This app will need to store the content of each user's information.  Each class in 
models.py is a database table. Each attribute/variable of the model represents a database field. 
You specify a data type and maybe some further attributes (e.g. max_length) for each attribute."""


from django.contrib.auth.models import User


class UserInterest(models.Model):
    name = models.CharField(max_length=65, unique=True)
    normalised_name = models.CharField(max_length=65, unique=True)

    def __str__(self):
        return self.name


class UserPersona(models.Model):
    name = models.CharField(max_length=65, unique=True)
    normalised_name = models.CharField(max_length=65, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_full_name_displayed = models.BooleanField(default=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200,blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)

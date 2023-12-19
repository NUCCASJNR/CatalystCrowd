#!/usr/bin/env python3

"""Contains signup form"""

from django.contrib.auth.forms import UserCreationForm
from crowd_funding.models.user import  CustomUser, models
from django import forms


class SignupForm(UserCreationForm):
    """
    Signup form
    """

    email: str = forms.EmailField(max_length=255)
    first_name: str = forms.CharField(max_length=50)
    last_name: str = forms.CharField(max_length=50)

    class Meta:
        model: models.Model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

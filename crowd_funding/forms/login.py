#!/usr/bin/env python3

"""Contains login form"""

from django import forms
from crowd_funding.models.user import CustomUser as User


class LoginForm(forms.Form):
    """
    @param username: str
    @param password: str
    """

    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())

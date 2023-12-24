#!/usr/bin/env pyhthon3

"""Contains a user profile update form"""

from django import forms
from crowd_funding.models.user import CustomUser


class ProfileForm(forms.ModelForm):
    """Profile Form"""

    class Meta:
        model = CustomUser
        fields = []

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(required=False)
        self.fields['email'] = forms.EmailField(required=False)
        self.fields['first_name'] = forms.CharField(required=False)
        self.fields['last_name'] = forms.CharField(required=False)
        self.fields['password'] = forms.CharField(required=False)
        self.fields['profile_picture'] = forms.CharField(required=False)

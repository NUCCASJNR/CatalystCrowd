#!/usr/bin/env python3

from django.contrib.auth.backends import ModelBackend
from crowd_funding.models.user import CustomUser


class EmailOrUsernameModelBackend(ModelBackend):
    """
    EmailOrUsernameModelBackend Class
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if the input is an email address
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = CustomUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

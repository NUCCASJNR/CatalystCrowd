#!/usr/bin/env python3

from django.contrib.auth.backends import ModelBackend
from crowd_funding.models.user import CustomUser as User


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
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

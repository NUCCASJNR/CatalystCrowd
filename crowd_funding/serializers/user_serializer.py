#!/usr/bin/env python3

"""Contains user serializer"""

from rest_framework import serializers
from crowd_funding.models.user import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['is_active', 'is_staff', 'is_superuser', 'last_login', 'profile_picture']

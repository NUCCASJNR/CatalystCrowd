#!/usr/bin/env python3

"""Contains user serializer"""

from rest_framework import serializers
from crowd_funding.models.user import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'password', 'username', 'id', 'email', 'created_at', 'updated_at']

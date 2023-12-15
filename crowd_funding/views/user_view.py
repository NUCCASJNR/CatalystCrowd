#!/usr/bin/env python3

"""Contains Users Views"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from crowd_funding.models.user import CustomUser
from crowd_funding.serializers.user_serializer import UserSerializer
from django.http import JsonResponse


class UserListView(APIView):
    """UserList view"""
    def get(self, request):
        users = CustomUser.get_all()
        users_list = [user.to_dict(user) for user in users]
        if users_list:
            return JsonResponse(users_list, status=status.HTTP_200_OK)
        return JsonResponse({"status": "Oops no users yet"})

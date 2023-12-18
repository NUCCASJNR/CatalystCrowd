#!/usr/bin/env python3

"""Contains Users Views"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from crowd_funding.models.user import CustomUser
from crowd_funding.serializers.user_serializer import UserSerializer
from django.http import JsonResponse
from django.core.exceptions import ValidationError


class UserListView(APIView):
    """UserList view"""
    def get(self, request):
        users = CustomUser.get_all()
        users_list = [user.to_dict(user) for user in users]
        if users_list:
            return JsonResponse(users_list, status=status.HTTP_200_OK, safe=False)
        return JsonResponse({"status": "Oops no users yet"})


class PostUserView(APIView):
    """"User Post View"""
    def post(self, request):
        """
        Post request handxler
        """
        serializer = UserSerializer(data=request.data)
        required_fields = ['username', 'email', 'last_name', 'first_name', 'password']
        for field in required_fields:
            if field not in serializer.initial_data:
                return JsonResponse({"error": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            new_user = serializer.save()
            user_dict = CustomUser.to_dict(new_user)
            return JsonResponse(user_dict, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserWithIdView(APIView):
    """Get user based on id view"""
    def get(self, request, user_id):
        """
        GET a user with id
        @param request: Request obj
        @param user_id: User id provided
        @return: user object in dict format
        """
        try:
            user = CustomUser.find_obj_by(**{'id': user_id})
            if user:
                user_dict = CustomUser.to_dict(user)
                return JsonResponse(user_dict, status=status.HTTP_200_OK)
        except ValidationError:
            return JsonResponse({'error': f"User with id {user_id} doesn't exist"})


class DeleteUserWithIdView(APIView):
    """Delete a user based on id view"""
    def delete(self, request, user_id):
        """
        Delete a user with id
        @param request: Request obj
        @param user_id: user id provided
        @return: A 200 response message
        """

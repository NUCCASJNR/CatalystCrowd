#!/usr/bin/env python3

"""Contains Project Views"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from crowd_funding.models.project import Project
from crowd_funding.serializers.project_serializer import ProjectSerializer
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from crowd_funding.models.user import CustomUser


class ProjectListView(APIView):
    """ProjectList view"""
    def get(self, request):
        """
        GET all projects
        @param request: Request obj
        @return: List of projects in dict format
        """
        projects = Project.get_all()
        projects_list = [project.to_dict(project) for project in projects]
        if projects_list:
            return JsonResponse(projects_list, status=status.HTTP_200_OK, safe=False)
        return JsonResponse({"status": "Oops no projects yet"})


class PostProjectView(APIView):
    """Project Post View"""
    def post(self, request):
        """
        Post request handler
        @param request: Request obj
        @return: Project object in dict format
        """
        serializer = ProjectSerializer(data=request.data)
        required_fields = ['user_id', 'project_name', 'description', 'target_amount', 'start_date', 'end_date']
        for field in required_fields:
            if field not in serializer.initial_data:
                return JsonResponse({"error": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            print(serializer.validated_data)
            new_project = Project.custom_save(**serializer.validated_data)
            user_id = CustomUser.to_dict(new_project.user_id)['id']
            project_dict = Project.to_dict(new_project)
            project_dict['user_id'] = user_id
            return JsonResponse(project_dict, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
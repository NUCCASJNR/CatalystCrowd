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
        projects_dict = [project.to_dict(project) for project in projects]
        print(projects_dict)
        for project in projects_dict:
            user_id = CustomUser.to_dict(project['user_id'])['id']
            project['user_id'] = user_id
        if projects_dict:
            return JsonResponse(projects_dict, status=status.HTTP_200_OK, safe=False)


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


class GetUserProjects(APIView):
    """Get user projects view"""
    def get(self, request, user_id):
        """
        List all the projects that belongs to a user
        @param request: Request obj
        @param user_id: User id provided
        @return: projects in dict format
        """
        try:
            projects = Project.find_obj_by(**{'user_id': user_id})
            if projects:
                projects_dict = Project.to_dict(projects)
                projects_dict['user_id'] = CustomUser.to_dict()
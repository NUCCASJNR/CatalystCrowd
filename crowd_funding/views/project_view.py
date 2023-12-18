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
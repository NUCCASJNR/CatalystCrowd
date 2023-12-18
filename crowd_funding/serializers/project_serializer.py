#!/usr/bin/env python3

"""Contains Project Serializer"""

from rest_framework import serializers
from crowd_funding.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Project Serializer"""
    class Meta:
        """Meta class"""
        model = Project
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')

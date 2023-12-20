#!/usr/bin/env python3

"""Contains a project form"""

from django import forms
from crowd_funding.models.project import Project


class ProjectForm(forms.ModelForm):
    """Project form"""
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'target_amount', 'start_date', 'end_date', 'project_picture']
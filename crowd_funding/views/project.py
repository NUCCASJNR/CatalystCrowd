#!/usr/bin/env python3

"""Contains project logic"""

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from crowd_funding.forms.project import ProjectForm
from crowd_funding.models.project import Project
from .login import login, dashboard


def create_project(request):
    """Create project view"""
    if not request.user.is_authenticated:
        return redirect(login)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            description = form.cleaned_data['description']
            target_amount = form.cleaned_data['target_amount']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            project_picture = form.cleaned_data['project_picture']
            category = form.cleaned_data['category']

            project_dict = {
                'project_name': project_name,
                'description': description,
                'target_amount': target_amount,
                'start_date': start_date,
                'end_date': end_date,
                'category': category,
                'project_picture': project_picture
            }
            project = Project.custom_save(**project_dict)
            print(project)
            return redirect(dashboard)
        else:
            # Print the form errors
            print(form.errors)
    else:
        form = ProjectForm()

    return render(request, 'crowd_funding/member/add-campaign.html', {'form': form})

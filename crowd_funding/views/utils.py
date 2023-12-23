#!/usr/bin/env python3

"""Contains views that would mostly be needed in each file"""
from django.db.models import QuerySet
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from crowd_funding.models.base_model import BaseModel
from crowd_funding.models.project import Project


def index(request):
    """Index view
    @param request: Request obj
    """
    projects: Project = Project.get_all().order_by('-created_at')
    return render(request, 'crowd_funding/index.html', {'projects': projects})


def about(request):
    """About view"""
    return render(request, 'crowd_funding/about.html')


def contact(request):
    """Contact view"""
    return render(request, 'crowd_funding/contact.html')


def all_projects(request):
    """Project view
    @param request: Request obj
    """
    projects = Project.get_all().order_by('-created_at')
    return render(request, 'crowd_funding/campaign-list.html', {'projects': projects})


def gallery(request):
    """
    Gallery view for displaying a user projects pictures
    @param request: Request obj
    @return: User projects pictures
    """
    pictures = Project.find_objs_by(**{'user_id': request.user.id})
    return render(request, 'crowd_funding/member/gallery.html', {'pictures': pictures})

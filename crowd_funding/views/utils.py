#!/usr/bin/env python3

"""Contains views that would mostly be needed in each file"""

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from crowd_funding.models.project import Project


def index(request):
    """Index view
    @param request: Request obj
    """
    projects = Project.get_all().order_by('-created_at')
    return render(request, 'crowd_funding/index.html', {'projects': projects})


def about(request):
    """About view"""
    return render(request, 'crowd_funding/about.html')


def contact(request):
    """Contact view"""
    return render(request, 'crowd_funding/contact.html')
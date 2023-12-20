#!/usr/bin/env python3

"""Contains views that would mostly be needed in each file"""

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


def index(request):
    """Index view"""
    return render(request, 'crowd_funding/index.html')


def about(request):
    """About view"""
    return render(request, 'crowd_funding/about.html')


def contact(request):
    """Contact view"""
    return render(request, 'crowd_funding/contact.html')
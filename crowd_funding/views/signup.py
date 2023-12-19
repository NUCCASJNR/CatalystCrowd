#!/usr/bin/env python3

"""Contains signup view."""


from django.shortcuts import render, redirect, reverse


def index(request):
    """Index view"""
    return render(request, 'crowd_funding/member/campaign-list.html')
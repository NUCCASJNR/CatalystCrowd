#!/usr/bin/env python3

"""Contains signup view."""


from django.shortcuts import render, redirect, reverse
from crowd_funding.forms.signup import SignupForm, CustomUser
from django.contrib import messages
from .login import dashboard, login
from django.contrib.auth import login as auth_login
from .user_api_view import GetUserWithIdView


def index(request):
    """Index view"""
    return render(request, 'crowd_funding/index.html')


def signup(request):
    """
    Handles user signup
    @param request: Request obj
    @return: redirect to user's dashboard if signup was successful
    """

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password1']

            user_dict = {
                'username': username,
                'email': email,
                'last_name': last_name,
                'first_name': first_name,
                'password': password
            }

            if CustomUser.find_obj_by(**{'email': email}):
                messages.error(request, 'Email already exists')
            if CustomUser.find_obj_by(**{'username': username}):
                messages.error(request, 'Username already exists')
            user = CustomUser.custom_save(**user_dict)
            print("User object before saving:", user)
            messages.success(request, 'Account created successfully')
            auth_login(request, user)
            return redirect(dashboard)
        else:
            print(form.errors)

    else:
        form = SignupForm()

    return render(request, 'crowd_funding/signup.html', {'form': form})

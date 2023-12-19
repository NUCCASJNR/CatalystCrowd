#!/usr/bin/env python3

"""Contains signup view."""


from django.shortcuts import render, redirect, reverse
from crowd_funding.forms.signup import SignupForm, CustomUser
from django.contrib import messages
from .login import dashboard


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

            if user:
                messages.success(request, 'Account created successfully')
                return redirect(reverse(dashboard, kwargs={'user_id': user.id}))
            else:
                print(form.errors)
        else:
            # The form is not valid, render the form with errors
            messages.error(request, 'Invalid form submission')
    else:
        # This is a GET request, instantiate a blank form
        form = SignupForm()

    return render(request, 'crowd_funding/signup.html', {'form': form})

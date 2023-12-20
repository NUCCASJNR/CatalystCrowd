#!/usr/bin/env python3

"""User login view"""

from django.shortcuts import render, redirect
from django.contrib import messages
from crowd_funding.forms.login import User, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from crowd_funding.models.project import Project

def login(request):
    """Login view handler"""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                print("User logged in:", str(request.user))  # Use UUID instead of ID
                if user:
                    auth_login(request, user)
                    messages.success(request, f'Hi {username.title()} Welcome to catalyst crowd')
                    return redirect('dashboard')
            except Exception as e:
                print(request, str(e))
    else:
        form = LoginForm()
    return render(request, 'crowd_funding/login.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    query = {'user_id': request.user.id}
    print(request.user.id)
    projects_count = Project.filter_count(**query)
    return render(request, 'crowd_funding/dashboard.html', {'projects_count': projects_count})

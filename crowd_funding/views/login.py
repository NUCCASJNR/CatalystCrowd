#!/usr/bin/env python3

"""User login view"""

from django.shortcuts import render, redirect
from django.contrib import messages
from crowd_funding.forms.login import User, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):
    """Login view handler"""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                print("User logged in:", request.user)
                if user:
                    print(f'Successful login by {username}')
                    auth_login(request, user)
                    print("Redirecting to dashboard")
                    messages.success(request, f'Hi {username.title()}, Welcome Back!')
                    print("Redirecting to dashboard")
                    return redirect('crowd_funding.dashboard')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = LoginForm()
    return render(request, 'crowd_funding/login.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'crowd_funding/member/dashboard.html')

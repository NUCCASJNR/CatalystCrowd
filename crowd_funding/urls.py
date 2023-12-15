#!/usr/bin/env python3

from django.urls import path
from crowd_funding.views.user_view import (
    UserListView,
    PostUserView
)

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('add_user/', PostUserView.as_view())
]

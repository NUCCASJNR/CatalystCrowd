#!/usr/bin/env python3

from django.urls import path
from crowd_funding.views.user_view import (
    UserListView,
    PostUserView,
    GetUserWithIdView,
    DeleteUserWithIdView
)

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('add_user/', PostUserView.as_view()),
    path('user/<str:user_id>/', GetUserWithIdView.as_view()),
    path('del_user/<str:user_id>/', DeleteUserWithIdView.as_view())
]

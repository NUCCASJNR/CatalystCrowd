#!/usr/bin/env python3

from django.urls import path
from crowd_funding.views.user_api_view import (
    UserListView,
    PostUserView,
    GetUserWithIdView,
    DeleteUserWithIdView,
    UpdateUserWithIdView,
    CountUsers
)

from crowd_funding.views.project_api_view import (
    CountProjects,
    ProjectListView,
    PostProjectView,
    GetUserProjects
)

urlpatterns = [
    path('api/users/', UserListView.as_view()),
    path('api/add_user/', PostUserView.as_view()),
    path('api/user/<str:user_id>/', GetUserWithIdView.as_view()),
    path('api/del_user/<str:user_id>/', DeleteUserWithIdView.as_view()),
    path('api/users_count/', CountUsers.as_view()),
    path('api/update_user/<str:user_id>/', UpdateUserWithIdView.as_view()),
    path('api/projects/', ProjectListView.as_view()),
    path('api/add_project/', PostProjectView.as_view()),
    path('api/get_user_projects/<str:user_id>/', GetUserProjects.as_view()),
    path('api/projects_count/', CountProjects.as_view())
]

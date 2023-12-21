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
    CountUserProjects,
    ProjectListView,
    PostProjectView,
    GetUserProjects
)

from crowd_funding.views.signup import index, signup
from crowd_funding.views.login import dashboard, login, logout
from crowd_funding.views.utils import about, contact
from crowd_funding.views.project import create_project
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
    path('api/projects_count/', CountProjects.as_view()),
    path('api/user_projects_count/<str:user_id>', CountUserProjects.as_view()),
    path('', index, name='index'),
    path('auth/signup', signup, name='signup'),
    path('dashboard', dashboard, name='dashboard'),
    path('auth/login', login, name='login'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('create_project', create_project, name='create_project'),
    path('auth/logout', logout, name='logout')
]

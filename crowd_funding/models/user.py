#!/usr/bin/env python3

"""Contains user model."""

from crowd_funding.models.base_model import BaseModel, models
from django.contrib.auth.models import AbstractUser, Group, Permission
from crowd_funding.storage import UserProfileImageStorage


def user_profile_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_profile_images/<user_id>/<filename>
    return f'user_profile_images/{instance.id}/{filename}'


class CustomUser(AbstractUser, BaseModel):
    """User class"""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(max_length=255, null=True, upload_to=user_profile_image_path)

    groups = models.ManyToManyField(Group, blank=True, related_name='crowdfunding_user_groups')

    # Add related_name to resolve clashes with auth.User.user_permissions
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='crowdfunding_user_permissions')

    class Meta:
        """Meta class"""
        db_table = 'users'
    #
    # def __str__(self):
    #     return f"Welcome to CatalystCrowd {self.username}"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

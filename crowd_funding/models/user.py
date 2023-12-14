#!/usr/bin/env python3

"""Contains user model."""

from crowd_funding.models.base_model import BaseModel, models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, BaseModel):
    """User class"""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(max_length=255, null=True)

    class Meta:
        """Meta class"""
        db_table = 'users'

    def __str__(self):
        return "f Welcome to CatalystCrowd {self.username}"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

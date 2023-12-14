#!/usr/bin/env python3

"""Contains contribution model."""

from crowd_funding.models.base_model import BaseModel, models
from crowd_funding.models.project import CustomUser, Project


class Contribution(BaseModel):
    """Contribution class"""
    user_id = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, blank=False, db_column='user_id')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, blank=False, db_column='project_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

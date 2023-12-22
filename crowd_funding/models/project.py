#!/usr/bin/env python3

"""
Project Model
"""

from crowd_funding.models.base_model import BaseModel, models
from crowd_funding.models.user import CustomUser
from decimal import Decimal
from crowd_funding.storage import ProjectImageStorage


def default_project_picture():
    return '/CatalystCrowd/crowd_funding/static/crowd_funding/assets/img/logo.png'


def project_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/project_images/<project_id>/<filename>
    return f'project_images/{instance.id}/{filename}'


class Project(BaseModel):
    """
    Project class docs soon ....
    """
    user_id = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, blank=False, db_column='user_id')
    project_name = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=255, default='miscellaneous')
    description = models.TextField(blank=False)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    project_picture = models.ImageField(blank=True, default=default_project_picture,
                                        upload_to=project_image_path)
    amount_left = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'projects'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set default values if None
        self.raised_amount = self.raised_amount or 0
        self.target_amount = self.target_amount or 0

        # Calculate amount_left
        self.amount_left = Decimal(self.target_amount - self.raised_amount)


#!/usr/bin/env python3

"""
Project Model
"""

from crowd_funding.models.base_model import BaseModel, models
from crowd_funding.models.user import CustomUser
from decimal import Decimal


class Project(BaseModel):
    """
    Project class docs soon ....
    """
    user_id = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, blank=False, db_column='user_id')
    project_name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    project_picture = models.ImageField(blank=True)
    amount_left = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'projects'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.raised_amount is None:
            self.raised_amount = Decimal(0)
        self.amount_left = Decimal(self.target_amount - self.raised_amount)

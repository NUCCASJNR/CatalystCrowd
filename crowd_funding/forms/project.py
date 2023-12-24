#!/usr/bin/env python3

"""Contains a project form"""

from django import forms
from crowd_funding.models.project import Project
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime


class ProjectForm(forms.ModelForm):
    """Project form"""

    class Meta:
        model = Project
        fields = ['category', 'project_name', 'description', 'target_amount', 'start_date',
                  'end_date', 'project_picture']

    def clean_start_date(self):
        """
        Validates project start date
        @return: Validation Error if it is else it returns the date
        """
        start_date = self.cleaned_data['start_date']
        current_datetime = timezone.now()

        if start_date < current_datetime:
            raise ValidationError("Start date must be the current date or a future date.")

        return start_date

    # def clean_end_date(self):
    #     start_date = self.cleaned_data.get('start_date')
    #     end_date = self.cleaned_data.get('end_date')
    #
    #     if start_date and end_date and end_date <= start_date:
    #         raise forms.ValidationError("End date must be after the start date.")
    #
    #     return end_date


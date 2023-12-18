#!/usr/bin/env python3

"""Base model for CrowdFunding"""

from datetime import datetime
from django.db import models
from typing import Any, Dict, Optional, List, Union
from uuid import uuid4


class BaseModel(models.Model):
    """Base model for CrowdFunding
    Every other classes should inherit this class
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    @classmethod
    def custom_save(cls, **kwargs: Dict[str, Any]):
        """
        Saves an instance of the class
        """
        # cls.updated_at = datetime.now()
        instance = cls.objects.create(**kwargs)
        return instance

    @classmethod
    def get_all(cls):
        """Get all objs of a cls"""
        return cls.objects.all()

    @classmethod
    def custom_delete(cls, **kwargs: Dict[str, Any]):
        """
        Deletes an instance of the class Based
        on the kwargs filter
        """
        instance = cls.objects.filter(**kwargs)
        instance.delete()

    @classmethod
    def custom_update(cls, filter_kwargs: Dict[str, Any], update_kwargs: Dict[str, Any]):
        """
        Updates an instance of the class based on the filter_kwargs and update_kwargs.
        """
        instance = cls.objects.filter(**filter_kwargs)
        instance.update(**update_kwargs)
        return cls.objects.get(**filter_kwargs)  # Return the updated instance

    @classmethod
    def find_objs_by(cls, **kwargs: Dict[str, Any]):
        """
        Finds an instance of the class Based
        on the kwargs
        """
        try:
            instance = cls.objects.filter(**kwargs)
            return instance
        except cls.DoesNotExist:
            return "No instances found"

    @classmethod
    def find_obj_by(cls, **kwargs: Dict[str, Any]):
        """
        Finds an instance of the class Based
        on the kwargs
        """
        try:
            instance = cls.objects.get(**kwargs)
            return instance
        except cls.DoesNotExist:
            return "No such instance"

    @classmethod
    def filter_count(cls, **kwargs: Dict[str, Any]):
        """
        Counts the number of instances of the class
        """
        return cls.objects.filter(**kwargs).count()

    @classmethod
    def count(cls):
        """
        Counts the number of instances of the class
        """
        return cls.objects.count()

    @classmethod
    def to_dict(cls, obj: Any) -> Dict[str, Any]:
        """
        Converts the object to a dictionary
        @type obj: object
        """
        
        model_dict = {}
        for field in obj._meta.fields:
            field_name = field.name
            field_value = getattr(obj, field_name)
            # convert special types to a serializable format if needed
            if isinstance(field, models.DateTimeField):
                field_value = field_value.isoformat() if field_value else None
            elif isinstance(field, models.UUIDField):
                field_value = str(field_value)
            elif isinstance(field, models.ImageField):
                field_value = field_value.url if field_value else None
            model_dict[field_name] = field_value
            
        return model_dict

